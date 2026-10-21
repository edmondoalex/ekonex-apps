# Aggiornare Dahua Access Reader alla 4.0.0

Questa versione serve a provare il flusso di aggiornamento Driver: nessuna
nuova funzione del lettore, configurazioni e registri conservati.

1. Aggiorna il catalogo App e installa **Ekonex Installer 0.1.0-test53**.
2. Riapri e-Control, vai in **Driver Ekonex** e apri **Dahua Access Reader**.
3. Verifica versione disponibile **4.0.0** e premi **Aggiorna Driver**.
4. Premi **Verifica aggiornamento, backup e licenza** e controlla l'esito.
5. Spunta il consenso e premi **Aggiorna con Ekonex**.
6. Attendi la verifica del backup e l'installazione. Quando richiesto,
   conferma separatamente il riavvio di **Home Assistant Core**.
7. Attendi **completed / 100%**, poi verifica versione **4.0.0**, owner **EKONEX**
   e inventario invariato. Esegui separatamente la normale verifica funzionale.

Non disinstallare il Driver, non cancellare configurazioni e non forzare un
riavvio mentre il backup o l'installazione sono in corso. L'aggiornamento
dell'App Installer non avvia aggiornamenti dei Driver. Il riavvio di Core
interrompe temporaneamente Home Assistant: non e un riavvio dell'intero host.

Il rollback usa il backup di quel job, non una copia generica. Se compare un
blocco o uno stato di recupero, fermati e conserva la diagnostica redatta.

La fonte 4.0.0 e qualificata da HACS, Hassfest e test di regressione sul commit
`18aa1a9ca6c513835b26a64aa1b3465d179cbdcb`, CI `39599008071`.
Il pacchetto conserva tutti i file della 3.0.3 salvo la versione nel manifest.

Installer53: sorgente `8c68331e7b8ed3336060a2f33ce7204a732751d1`,
CI privata `39599926220` SUCCESS, 497 test Linux in ciascuno dei due job,
test di avvio/arresto e accesso diretto negato superati.
Immagine: `ghcr.io/edmondoalex/ekonex-installer:0.1.0-test53`, digest
`sha256:b543805c66a11074dbea1f13e45a7c992948732c8f7258d0525115cf47908efc`.
