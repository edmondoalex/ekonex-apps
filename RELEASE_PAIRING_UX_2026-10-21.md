# Associazione e aggiornamenti guidati

Release qualificate: e-Control fonte645b991846e8e39210ccec1de85bf78c69e53ba8,
builderf68c90c15deccac9a1e7ed62b677cdb70483a53d, CI39609970113SUCCESS,
724PASS14skip, parity202file e smoke/arrestoPASS.
Digest `sha256:c9a6178c3328fe6cb462223472e7eeca0ddaead74e4534f4770ee65938e0e8d7`.
Installer fonte0608d3dfe5f2a5ab660b6f4ae7c743030db11e51, CI39610604407SUCCESS,
514PASS2skip per job, stdin entrypoint reale/no segreti log/arrestoPASS.
Digest `sha256:2428d2d5d421319332de2e4ba77eb221bf625bba0ef185380e40505c43646aab`.

1. Aggiornare Ekonex Installer a **0.1.0-test54**.
2. Aggiornare e-Control a **0.1.671-dist1** e riaprire la pagina.
3. Su un impianto non associato, aprire Driver e scegliere **Associa questo impianto** come amministratore, con consenso esplicito.
4. Attendere conferma dell'associazione e caricamento del catalogo. Non occorre aprire Installer o copiare codici.
5. Per aggiornare un Driver: selezione -> verifica -> riepilogo e consenso -> avanzamento. Confermare separatamente il riavvio quando richiesto.

Menu laterale disponibile anche su App, Driver, dettagli e flusso. Messaggio catalogo: **Aggiornamento catalogo App in corso…**.

Le associazioni esistenti non vengono sostituite. Dopo un esito di consegna incerto attendere tre minuti prima di riprovare con nuovo consenso. L'aggiornamento delle App non avvia automaticamente aggiornamenti Driver o associazioni.

Il bootstrap usa esclusivamente il canale amministrativo interno dello stesso impianto; codici e segreti non vengono mostrati nel browser. I permessi amministrativi locali restano necessari.
