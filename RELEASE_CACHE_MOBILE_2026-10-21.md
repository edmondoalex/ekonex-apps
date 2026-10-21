# Cache pagine e sinottico mobile

Aggiornamenti manuali: e-Control **0.1.672-dist1** ed e-Face **2.21.391-dist1**.

- e-Control: HTML non riutilizzabile dalla cache e link menu versionati, mantenendo prefissi e parametri. Test browser con vecchia pagina in cache: baseline difettosa riprodotta e correzione PASS.
- e-Face: corsia mobile riservata ai percorsi animati, senza sovrapposizione alle schede. Correzioni URL icona cat, slider verticale e struttura form SIP. Logica riscaldamento invariata.
- Gli avvisi Permissions-Policy non originano dal sorgente verificato: nessuna protezione rimossa. Il singolo reflow31ms non attesta un guasto.

e-Control0.1.672-dist1 fonte4739c25f510c85ff15078e2c407cd2966cfbb501, builder ea6f2209bdfd5a635c29e13815fae4a249a0c0c2; run39623080228 riepilogo ancora in_progress al controllo, unico job119301292568 completedSUCCESS con tutti gli stepSUCCESS:726PASS14skip/parity203file/health/deps/exit0. Digest sha256:ae8a3fd1e02411d4845bae1bfae9f5ca04426130ce1f18281499d370b1e8829d. e-Face2.21.391-dist1 fonte533b36ada325db24554bbbb816bfec8069ba3d73, builderc2212417083f576e6090cdafd9d6e78cd6f01b6c, CI39623498441SUCCESS689PASS0skip/parity226file/ownershipentrypoint/health/deps/exit0. Digest sha256:5a125157f24cf75f8994fdd2ea278a1af193642116dd9f453f478431cc98ac40.

Nessuna installazione o comando impianto automatico. Installer54 invariato; questa release non qualifica una nuova ricetta di migrazione Alexa legacy con companion391. Per tale operazione resta necessaria qualificazione coordinata separata, senza bypass dei blocchi.
