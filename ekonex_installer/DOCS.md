# Ekonex Installer - Test 0.1.0-test4

Candidata di collaudo **banco amd64**, sullo stesso Home Assistant.
Supporta e-Control0.1.393/0.1.566 verso0.1.566-dist1 ed e-Safe5.2.103/5.2.106
verso5.2.106-dist2. Non abilita gli altri sette prodotti o impianti operativi.
La verifica dei dati non equivale al collaudo delle periferiche.

## Procedura breve

1. Aggiorna il catalogo Ekonex Apps e Installer alla0.1.0-test4.
2. Mantieni ferme le copie originali e nuove dei prodotti da migrare.
3. Nella scheda del solo Installer disattiva temporaneamente Modalita protezione,
   poi riavvia Installer. Gli altri add-on mantengono la loro protezione.
4. Apri Interfaccia Web come amministratore. Analizza impianto, seleziona i prodotti.
5. Continua > Verifica prerequisiti. Usa GHCR gia configurato da Avvio:
   non reinserire token. Un registro presente non dimostra che il token sia valido;
   il download effettivo viene verificato dal Supervisor.
6. Continua > Conferma. Se una destinazione esiste, conferma separatamente la
   sostituzione dei suoi dati, che verranno prima salvati.
7. Avvia migrazione. Il programma crea e rilegge il backup nativo, installa da
   solo le copie mancanti, trasferisce dati/opzioni/porte e confronta i file.
8. Attendi il risultato. Scarica il report e conserva anche il backup nativo
   da Home Assistant fuori dal mini PC. Non disinstallare gli originali.
9. Arresta Installer e riattiva la sua protezione. Vecchie e nuove copie restano
   ferme/manuali, senza watchdog o aggiornamenti automatici. Avvio e collaudo
   delle sole copie nuove sono un passaggio successivo consapevole.

## Interruzioni ed errori

Non ripetere l'operazione o eliminare copie. Riapri Installer: il diario resta.
Durante un errore dopo l'inizio del trasferimento prova il ripristino della
destinazione, conservando tutte le copie. Dopo un riavvio/interruzione usa il
pulsante **Ripristina destinazioni**, con la sua conferma; mai ripresa automatica.
Se compare intervento richiesto, conserva report e backup e non avviare le copie.
Un'installazione fallita prima della copia non altera i dati originali; eventuali
nuove copie installate restano disponibili ma ferme.

I dati originali non vengono cancellati. La procedura non riscrive arbitrariamente
URL, identificativi MQTT, registri HA o collegamenti salvati: verificare i
collegamenti tra applicazioni nel successivo collaudo. La configurazione delle
porte e le opzioni vengono confrontate tramite API Supervisor.

## Accesso di manutenzione

Solo temporaneamente: host PID, SYS_PTRACE, DAC_READ_SEARCH, AppArmor disabilitato,
socket Docker usato esclusivamente per GET/inspect, backup montato in lettura.
Niente full_access, shell sul Supervisor, Docker exec/scritture o porte pubbliche.
Accesso dati limitato agli identificativi e-Control/e-Safe previsti, con ancoraggio
al processo Supervisor verificato e al volume privato dello stesso Installer.
Link, file speciali, sorgenti attive e versioni diverse bloccano la copia.

Backup nativo locale non cifrato e copie private contengono le configurazioni,
quindi possono contenere password degli add-on: custodirli come dati sensibili.
Il diario privato dell'Installer e in /data/maintenance, protetto0700/0600.
Non inviarlo in chat; il report scaricabile esclude opzioni e segreti.
Il token GHCR resta nel registro nativo Supervisor, non nel diario migrazione.

Collaudo eseguito su file sintetici e container Linux isolati, incluse interruzioni,
ripristino, permessi, volumi e blocco copie attive. Il primo collaudo su questo
impianto e sulle periferiche reali resta da eseguire. Nessuna garanzia di zero bug.
