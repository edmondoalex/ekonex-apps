"""Public bootstrap: GHCR credential provisioning only. No migration code."""
import base64
import json
import os
from pathlib import Path
import re
import secrets
import threading
import urllib.parse
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

STATIC = Path(__file__).parent / "static"
PACKAGE = "ekonex-installer"
TAG = "0.1.0-test2"
INSTALLED_PACKAGES = {
    "e_hdl_buspro_mqtt": "ekonex-econtrol-pilot", "e_face_x4": "ekonex-eface-pilot",
    "ksenia_lares_addon": "ekonex-esafe", "irrigazione_dashboard_v2": "ekonex-edry",
    "e_sunmind": "ekonex-esunmind", "e_therm_plus_ks": "ekonex-ethermplus",
    "e_thermomind": "ekonex-ethermomind", "asterisk_eface": "ekonex-evoip",
    "energy_core": "ekonex-energycore",
}


class SafeError(Exception):
    pass


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        return None


class Transport:
    """Fixed endpoint allowlists; no redirects, environment proxies or error echo."""
    def __init__(self, supervisor_token=None, opener=None):
        self._token = supervisor_token if supervisor_token is not None else os.environ.get("SUPERVISOR_TOKEN", "")
        self._opener = opener or urllib.request.build_opener(urllib.request.ProxyHandler({}), NoRedirect())

    def _request(self, url, method="GET", headers=None, payload=None, head=False):
        request = urllib.request.Request(url, method=method, headers=headers or {},
            data=None if payload is None else json.dumps(payload).encode())
        try:
            with self._opener.open(request, timeout=15) as response:
                raw = b"" if head else response.read(1024**2 + 1)
                if len(raw) > 1024**2:
                    raise ValueError()
                result = {} if head else json.loads(raw)
                if not isinstance(result, dict):
                    raise ValueError()
                return result, {k.lower(): v for k, v in response.headers.items()}
        except Exception:
            raise SafeError("Verifica non riuscita: controlla connessione, token, scadenza e permessi. Nessun dettaglio sensibile registrato.") from None

    def supervisor(self, path, payload=None):
        allowed = ("/auth/list", "/docker/registries", "/addons")
        if path not in allowed or not self._token or (payload is not None and path != "/docker/registries"):
            raise SafeError("Operazione Supervisor non consentita.")
        value, _ = self._request("http://supervisor" + path, "POST" if payload is not None else "GET",
            {"Authorization": "Bearer " + self._token, "Content-Type": "application/json"}, payload)
        if value.get("result") != "ok":
            raise SafeError("Supervisor non ha confermato l'operazione.")
        return value.get("data", {})

    def github(self, path, token):
        if path not in ("/user", *("/users/edmondoalex/packages/container/" + p for p in [PACKAGE, *INSTALLED_PACKAGES.values()])):
            raise SafeError("Endpoint GitHub non consentito.")
        return self._request("https://api.github.com" + path, headers={
            "Authorization": "Bearer " + token, "Accept": "application/vnd.github+json",
            "User-Agent": "Ekonex-Installer-Setup"})

    def manifest(self, username, token, package=PACKAGE, tag=TAG):
        if package not in [PACKAGE, *INSTALLED_PACKAGES.values()] or not re.fullmatch(r"[A-Za-z0-9_][A-Za-z0-9_.-]{0,127}", tag):
            raise SafeError("Pacchetto da verificare non valido.")
        basic = base64.b64encode((username + ":" + token).encode()).decode()
        query = urllib.parse.urlencode({"service": "ghcr.io", "scope": "repository:edmondoalex/" + package + ":pull"})
        auth, _ = self._request("https://ghcr.io/token?" + query, headers={"Authorization": "Basic " + basic})
        bearer = auth.get("token")
        if not isinstance(bearer, str) or not bearer or len(bearer) > 16384 or any(c.isspace() for c in bearer):
            raise SafeError("GHCR non ha concesso l'accesso al pacchetto di prova.")
        _, headers = self._request("https://ghcr.io/v2/edmondoalex/" + package + "/manifests/" + tag,
            method="HEAD", head=True, headers={"Authorization": "Bearer " + bearer,
            "Accept": "application/vnd.docker.distribution.manifest.v2+json,application/vnd.oci.image.manifest.v1+json,application/vnd.oci.image.index.v1+json"})
        digest = headers.get("docker-content-digest", "")
        if not re.fullmatch(r"sha256:[a-f0-9]{64}", digest):
            raise SafeError("Manifest GHCR non verificato.")
        return digest


class Setup:
    def __init__(self, transport=None):
        self.transport = transport or Transport()
        self.csrf = secrets.token_urlsafe(32)
        self.lock = threading.Lock()

    def admin(self, user_id, username):
        if not user_id or not username:
            return False
        users = self.transport.supervisor("/auth/list").get("users")
        if not isinstance(users, list):
            return False
        matches = [u for u in users if isinstance(u, dict) and u.get("username") == username]
        if len(matches) != 1 or matches[0].get("is_active") is not True:
            return False
        user = matches[0]
        return user.get("is_owner") is True or (isinstance(user.get("group_ids"), list) and "system-admin" in user["group_ids"])

    def registry(self):
        response = self.transport.supervisor("/docker/registries")
        registries = response.get("registries")
        if not isinstance(registries, dict):
            raise SafeError("Stato registro non leggibile. Nessuna modifica consentita.")
        entry = registries.get("ghcr.io")
        return {"configured": "ghcr.io" in registries,
                "username": str(entry.get("username", "")) if isinstance(entry, dict) else ""}

    def validate(self, payload):
        if not isinstance(payload, dict) or set(payload) - {"username", "token", "confirm", "replace", "expected_username"}:
            raise SafeError("Richiesta non valida.")
        username, token = payload.get("username"), payload.get("token")
        if not isinstance(username, str) or not re.fullmatch(r"[A-Za-z0-9-]{1,39}", username):
            raise SafeError("Inserisci il nome utente GitHub.")
        if not isinstance(token, str) or not 20 <= len(token) <= 512 or any(c.isspace() for c in token):
            raise SafeError("Inserisci il token classic, senza spazi.")
        user, headers = self.transport.github("/user", token)
        scopes = {s.strip() for s in headers.get("x-oauth-scopes", "").split(",") if s.strip()}
        if scopes != {"read:packages"}:
            raise SafeError("Usa un token classic con il solo permesso read:packages. Non usare repo o permessi di scrittura.")
        if str(user.get("login", "")).lower() != username.lower():
            raise SafeError("Il token appartiene a un altro account GitHub.")
        package, _ = self.transport.github("/users/edmondoalex/packages/container/" + PACKAGE, token)
        if package.get("visibility") != "private":
            raise SafeError("Il pacchetto privato di prova non e verificabile.")
        digest = self.transport.manifest(username, token)
        rows = self.transport.supervisor("/addons").get("addons")
        if not isinstance(rows, list):
            raise SafeError("Inventario non leggibile: verifica degli altri pacchetti non possibile.")
        checked = [PACKAGE + ":" + TAG]
        for row in rows:
            slug = str(row.get("slug", ""))
            short = slug.removeprefix("935e8182_")
            if not slug.startswith("935e8182_") or short not in INSTALLED_PACKAGES:
                continue
            product, version = INSTALLED_PACKAGES[short], str(row.get("version", ""))
            self.transport.manifest(username, token, product, version)
            checked.append(product + ":" + version)
        return {"username": username, "manifest_verified": True, "digest": digest,
                "expiration": headers.get("github-authentication-token-expiration"),
                "package": PACKAGE + ":" + TAG, "packages_verified": checked}

    def check(self, payload):
        if not self.lock.acquire(blocking=False):
            raise SafeError("Un controllo e gia in corso.")
        try:
            result = self.validate(payload)
            result["registry"] = self.registry()
            return result
        finally:
            self.lock.release()

    def save(self, payload):
        if not isinstance(payload, dict) or payload.get("confirm") is not True:
            raise SafeError("Conferma il salvataggio nel registro Home Assistant.")
        if not self.lock.acquire(blocking=False):
            raise SafeError("Un controllo e gia in corso.")
        try:
            before = self.registry()
            if before["configured"] and (payload.get("replace") is not True or payload.get("expected_username") != before["username"]):
                raise SafeError("GHCR e gia configurato: verifica il nuovo token e conferma esplicitamente la sostituzione.")
            verified = self.validate(payload)
            if self.registry() != before:
                raise SafeError("Il registro e cambiato durante il controllo. Nessuna sostituzione eseguita.")
            try:
                self.transport.supervisor("/docker/registries", {"ghcr.io": {
                    "username": payload["username"], "password": payload["token"]}})
                after = self.registry()
                if not after["configured"] or after["username"] != payload["username"]:
                    raise ValueError()
            except Exception:
                raise SafeError("Esito salvataggio incerto. Controlla lo stato del registro prima di riprovare; nessuna credenziale e stata cancellata.") from None
            return {**verified, "registered": True, "replaced": before["configured"], "supervisor_pull_tested": False,
                    "message": ("Credenziale sostituita e riletta." if before["configured"] else "Credenziale registrata.") +
                    " Ora installa o aggiorna Ekonex Installer - Test dal catalogo per verificare il download tramite Supervisor."}
        finally:
            self.lock.release()


def handler_for(app):
    class Handler(BaseHTTPRequestHandler):
        server_version = "EkonexSetup"
        def log_message(self, *args):
            pass

        def allowed(self):
            if self.client_address[0] != "172.30.32.2":
                return False
            try:
                return app.admin(self.headers.get("X-Remote-User-Id", ""), self.headers.get("X-Remote-User-Name", ""))
            except Exception:
                return False

        def send(self, code, value, mime="application/json; charset=utf-8"):
            body = value if isinstance(value, bytes) else json.dumps(value).encode()
            self.send_response(code)
            for key, val in {"Content-Type": mime, "Content-Length": str(len(body)),
                "Cache-Control": "no-store", "X-Content-Type-Options": "nosniff",
                "Referrer-Policy": "no-referrer",
                "Content-Security-Policy": "default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self'; connect-src 'self'; object-src 'none'; base-uri 'self'; form-action 'self'; frame-ancestors 'self'"}.items():
                self.send_header(key, val)
            self.end_headers()
            self.wfile.write(body)

        def do_GET(self):
            if not self.allowed():
                return self.send(403, {"error": "Apri da Home Assistant con un utente amministratore."})
            files = {"/": ("index.html", "text/html; charset=utf-8"), "/app.js": ("app.js", "text/javascript; charset=utf-8"),
                     "/style.css": ("style.css", "text/css; charset=utf-8"), "/logo.png": ("logo.png", "image/png")}
            if self.path in files:
                name, mime = files[self.path]
                return self.send(200, (STATIC / name).read_bytes(), mime)
            if self.path == "/api/status":
                try:
                    return self.send(200, {"csrf": app.csrf, "registry": app.registry()})
                except Exception:
                    return self.send(503, {"error": "Impossibile leggere il registro Supervisor."})
            return self.send(404, {"error": "Pagina non trovata."})

        def do_POST(self):
            if not self.allowed() or not secrets.compare_digest(self.headers.get("X-CSRF-Token", ""), app.csrf):
                return self.send(403, {"error": "Richiesta non autorizzata."})
            if self.headers.get("Content-Type", "").split(";")[0] != "application/json":
                return self.send(415, {"error": "Formato non supportato."})
            try:
                length = int(self.headers.get("Content-Length", "0"))
                if not 0 < length <= 4096 or self.headers.get("Transfer-Encoding"):
                    raise ValueError()
                payload = json.loads(self.rfile.read(length))
                if not isinstance(payload, dict):
                    raise ValueError()
            except (ValueError, UnicodeError):
                return self.send(400, {"error": "Richiesta non valida."})
            operation = {"/api/check": app.check, "/api/save": app.save}.get(self.path)
            if operation is None:
                return self.send(404, {"error": "Operazione non disponibile."})
            try:
                return self.send(200, operation(payload))
            except SafeError as error:
                return self.send(409, {"error": str(error)})
            except Exception:
                return self.send(500, {"error": "Operazione non riuscita. Nessun dettaglio sensibile registrato."})
    return Handler


if __name__ == "__main__":
    server = ThreadingHTTPServer(("0.0.0.0", 8720), handler_for(Setup()))
    server.daemon_threads = True
    print("Ekonex Installer - Avvio: disponibile solo tramite Ingress amministrativo", flush=True)
    server.serve_forever()
