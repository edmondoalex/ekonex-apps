# Ekonex Installer - Avvio

Avvio0.1.0-test9: gestione SIGTERM/SIGINT e arresto regolare con codice0 quando
non ci sono operazioni attive; log UTC. Verificato docker stop in CI. Credenziali
Supervisor e diario installazione invariati. Non arrestare durante salvataggio.
Installer privato resta0.1.0-test7; non vengono aggiornate copie gia presenti.

Aggiornamento Avvio0.1.0-test7: installa Installer privato0.1.0-test6 se assente.
Non aggiorna le copie gia presenti. Installer4 consente collaudo migrazione banco
con manutenzione esplicita, ma Avvio non abilita privilegi o migrazioni da solo.
I riferimenti Test2 seguenti descrivono la prima distribuzione storica.

Add-on pubblico di primo avvio: non richiede un token GHCR per installarsi.
Contiene configurazione credenziali, guida e installazione del solo Installer; nessun codice
degli add-on Ekonex privati o del loro trasferimento dati.

1. Aggiungi https://github.com/edmondoalex/ekonex-apps al catalogo Home Assistant.
2. Installa **Ekonex Installer - Avvio**. La prima installazione compila il piccolo
   pacchetto usando la base pubblica Python; Internet e necessario.
3. Avvia e apri Interfaccia Web come amministratore. Protezione attiva.
4. Apri la guida token. Crea un PAT classic dedicato con SOLO read:packages.
5. Inserisci utente e token, premi Verifica accesso GHCR.
6. Se GHCR non e configurato, conferma e premi Salva credenziale.
7. Il salvataggio avvia automaticamente l'installazione di **Ekonex Installer - Test**
   se assente. Attendi il risultato qui sotto, poi premi **Apri scheda Ekonex Installer**.
   Nella sua scheda premi Avvia e Interfaccia Web. Nessuna migrazione viene avviata.

Da Avvio **0.1.0-test3** non serve installare manualmente Installer dal catalogo.
Se gia presente viene lasciato invariato, senza aggiornamento, reinstallazione o
riavvio. In questo caso il nuovo token e verificato sul manifest, ma non e stato
provato un nuovo download completo. La versione installabile da questa release
e Installer privato **0.1.0-test2**; un catalogo diverso viene segnalato senza
installazioni. Il diario locale conserva solo stato e ID operazione, mai token.
Chiudere/riaprire la pagina non duplica l'installazione. Dopo un esito incerto non
si ripete automaticamente: controllare la scheda Installer e i log Supervisor.

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
Accessi remoti solo HTTPS. Questa versione installa soltanto Installer, non migra
ne installa/arresta gli altri prodotti. La protezione resta attiva.
Puoi arrestare Avvio dopo la configurazione; non e necessario lasciarlo in esecuzione.
