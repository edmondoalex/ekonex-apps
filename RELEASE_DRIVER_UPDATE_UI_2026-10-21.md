# e-Control 0.1.670-dist1 - aggiornamenti Driver

Release verificata: fonte `4eab53be5472b01c387c8839bb7b27e4c473f400`, builder
`d1e4ce5a2f46feafa2a46f8191506f454b019d00`, CI `39604949950` SUCCESS.
720 test locali PASS; Linux 706 PASS/14 skip; browser desktop/mobile PASS.
Immagine privata: `sha256:46067acf39e3d1e3f7a5299025e86b5422981ac0bc81facf4022664c5d9b6181`.
Parita esatta dei 201 file runtime/UI, smoke e arresto exit0 verificati.

Corregge tre problemi del percorso precedente:

- pulsante Aggiorna Driver assente nell'elenco;
- aggiornamenti gia gestiti da EKONEX indicati come migrazioni;
- nuova versione visibile nel catalogo ma rifiutata dal controllo statico
  del consumer prima dell'aggiornamento.

## Procedura

1. Nella sezione App aggiorna **e-Control a 0.1.670-dist1**.
2. Per Dahua Access Reader4.0.0 verifica anche **Installer0.1.0-test53**.
3. Riapri e-Control e vai su **Driver -> Dahua Access Reader**.
4. Nella scheda espansa vedrai **Aggiornamento disponibile** e **Aggiorna Driver**.
5. Premi **Aggiorna Driver**: si apre il flusso sul prodotto selezionato.
6. Esegui la verifica di aggiornamento, backup e licenza, leggi il riepilogo,
   spunta il consenso e premi **Aggiorna con Ekonex**.
7. Conferma separatamente il riavvio di **Home Assistant Core** quando richiesto.
   Attendi completamento e controlla versione4.0.0 e inventario invariato.

Un Driver HACS mostra invece **Migrazione richiesta / Migra Driver**.
Se manca una licenza o la compatibilita non e verificata, la schermata mostra
il motivo del blocco e non propone un'operazione pronta.

Il target e verificato contro il catalogo autorevole dell'Installer prima
di preflight e creazione job. Una versione cambiata dopo la verifica richiede
una nuova verifica e un nuovo consenso: non viene sostituita automaticamente.

L'aggiornamento dell'App e-Control non aggiorna i Driver e non riavvia Core.
Nessuna reinstallazione, cancellazione dati o comando al lettore e necessario.
