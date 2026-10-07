# Ekonex Apps

Home Assistant catalog. Product source and container packages remain private.
The only public executable code here is the small first-run credential setup tool.
Only amd64 is currently validated for the included releases.

## Primo avvio senza credenziali GHCR

1. Installa **Ekonex Installer - Avvio**: non richiede credenziali GHCR.
2. Avvialo e apri Interfaccia Web come amministratore, con protezione attiva.
3. Segui la guida popup per il token classic read:packages, verifica e salva.
4. Installa **Ekonex Installer - Test** per collaudare il download privato.

Avvio configura il registro e permette di rinnovare una credenziale esistente solo dopo verifica del nuovo token e conferma esplicita di sostituzione. Non riavvia gli add-on.
Installer - Test esegue solo analisi: la migrazione reale non e ancora abilitata.
Non disinstallare gli add-on originali per effettuare questa prova.
Guida completa: [primo avvio](ekonex_setup/DOCS.md).

Existing installations on other catalogs are not migrated by adding this repository.
Migration requires a verified backup and the dedicated installer procedure to preserve data.
Initial boot is manual to prevent two hardware gateways starting together during migration.
The installer restores the intended boot policy after successful verification.
Automatic updates are not enabled by this catalog.

Distribution versions dist1/dist2 identify packaging revisions, not additional app features.
