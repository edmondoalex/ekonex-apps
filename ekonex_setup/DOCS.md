# Ekonex Installer - Avvio

Add-on pubblico di primo avvio: non richiede un token GHCR per installarsi.
Contiene esclusivamente configurazione credenziali e guida; nessun codice
degli add-on Ekonex privati o del loro trasferimento dati.

1. Aggiungi https://github.com/edmondoalex/ekonex-apps al catalogo Home Assistant.
2. Installa **Ekonex Installer - Avvio**. La prima installazione compila il piccolo
   pacchetto usando la base pubblica Python; Internet e necessario.
3. Avvia e apri Interfaccia Web come amministratore. Protezione attiva.
4. Apri la guida token. Crea un PAT classic dedicato con SOLO read:packages.
5. Inserisci utente e token, premi Verifica accesso GHCR.
6. Se GHCR non e configurato, conferma e premi Salva credenziale.
7. Installa **Ekonex Installer - Test** dallo stesso catalogo: verifica cosi
   anche il download privato effettuato dal Supervisor.

Verifica accesso controlla identita GitHub, permessi minimi, accesso al pacchetto
privato ekonex-installer e al suo manifest GHCR. NON equivale al download completo
dell'immagine tramite Supervisor: questo viene provato al punto 7.
Il token e custodito dal Supervisor nel registro nativo, non in opzioni/file
dell'add-on. La persistenza si controlla tornando nella UI dopo il riavvio
dell'add-on e provando l'installazione privata.

## Rinnovo di un token scaduto (0.1.0-test2)

Se ghcr.io e gia presente, inserisci e verifica il nuovo token. Sono verificati
anche i pacchetti Ekonex privati gia installati, non soltanto Installer.
Spunta sia la conferma registrazione sia **Sostituisci la credenziale GHCR
esistente**, poi premi Sostituisci credenziale. La voce viene aggiornata tramite
Supervisor senza cancellazioni, riavvii o reinstallazioni degli add-on.
Non revocare il vecchio token ancora valido prima di aver collaudato quello nuovo.
Se il salvataggio ha esito incerto, rileggi lo stato e prova un download: la sola
presenza dello stesso nome utente non prova quale token sia memorizzato.
La lettura nativa non restituisce il vecchio segreto, quindi non e possibile
promettere rollback automatico della credenziale precedente.

Nessuna cancellazione o sostituzione automatica. Nessun token in chat, URL, screenshot o cartelle condivise.
Accessi remoti solo HTTPS. Questa versione non migra, installa o arresta prodotti.
Puoi arrestare Avvio dopo la configurazione; non e necessario lasciarlo in esecuzione.
