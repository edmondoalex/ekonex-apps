# Aggiornamento coordinato e-Face / Installer

Versioni: e-Face `2.21.390-dist1` e Ekonex Installer `0.1.0-test52`.

Installer52 aggiunge il riconoscimento esatto del manifest Alexa1.1.0 con
fine riga Windows (CRLF) distribuito dal pacchetto e-Face390. La51 poteva
mostrare owner UNKNOWN e compatibilita da verificare. Nessun file installato
viene normalizzato o modificato dal preflight; manifest diversi restano negati.
Se e-Face390 e gia installata, aggiornare soltanto Installer.

Questa release corregge il packaging del controllo ownership Alexa in e-Face.
Installer riconosce la nuova versione qualificata; e-Face `2.21.389-dist1` e
versioni sconosciute restano bloccate per la migrazione Alexa.

## Aggiornamento manuale

1. Aggiorna l'elenco App nel portale e-Control.
2. Aggiorna e-Face X4 a `2.21.390-dist1` e verifica che sia avviata.
3. Aggiorna Ekonex Installer a `0.1.0-test52` e verifica che sia avviato.
4. Riapri Migrazione con Ekonex dal menu generale, senza riusare un dettaglio
   e-Voice gia aggiornato. Seleziona e-Face Alexa, destinazione `2.0.0`.
5. Esegui nuovamente la verifica di compatibilita, licenza e backup.
6. Solo con verifica positiva, conferma l'aggiornamento e poi il riavvio
   separato richiesto dal flusso. Al termine verifica versione e owner EKONEX.

Non disinstallare le App e non ripetere le migrazioni gia concluse degli altri
Driver. Non forzare il blocco di compatibilita e non fermare la vecchia App
per aggirarlo. Configurazioni, licenze e backup restano gestiti dal flusso
esistente; la pubblicazione non avvia aggiornamenti o migrazioni automatiche.

Le prove di laboratorio non sostituiscono il collaudo funzionale Alexa sul
proprio impianto. Se il nuovo preflight segnala altri motivi di blocco, fermarsi
e leggere la diagnostica prima di procedere.
