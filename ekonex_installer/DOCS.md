# Ekonex Installer - Test 0.1.0-test2

Versione sperimentale amd64: analizza gli add-on installati e mostra la guida token.
NON esegue backup, migrazioni, installazioni, arresti o modifiche alle credenziali.
Non disinstallare i vecchi add-on per provare questa versione.

## Installazione nel mini PC

1. Se GHCR non e configurato, installare prima **Ekonex Installer - Avvio**:
   e pubblico e permette di verificare/salvare la prima credenziale con guida popup.
   Se gia configurato, usare la propria credenziale valida senza cancellarla.
2. Aggiungere il catalogo https://github.com/edmondoalex/ekonex-apps
   oppure aggiornarlo se e gia presente.
3. Cercare Ekonex Installer - Test, installare e avviare.
4. Aprire Interfaccia Web con un utente Home Assistant amministratore.
   Lasciare attiva la modalita protezione: non servono privilegi host.
5. Premere Analizza impianto. Controllare gli slug originali/nuovi e le versioni.
6. Continua > Guida credenziali apre il popup anche se le versioni sono bloccate.
   I campi token e il pulsante migrazione rimangono disabilitati intenzionalmente.

Se compare 401 durante il download, controllare il registro ghcr.io, la scadenza
del token e i permessi del suo account sul pacchetto ekonex-installer.
Non inserire password o token in chat o screenshot.

Se l'interfaccia risponde 403, controllare l'utente amministratore e aprire
tramite Home Assistant, non direttamente tramite IP/porta.

La prova non qualifica la compatibilita delle vecchie configurazioni e non
certifica un ripristino. Le operazioni reali arriveranno dopo il collaudo separato.
