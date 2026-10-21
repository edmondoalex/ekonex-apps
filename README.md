# Ekonex Apps

## Associazione da e-Control e aggiornamento guidato

Aggiornare prima **Installer0.1.0-test54**, poi **e-Control0.1.671-dist1**.
L'amministratore puo associare l'impianto direttamente da e-Control, senza
aprire Installer o copiare codici. Menu laterale condiviso e flusso aggiornamento
compatto con verifica, consenso e riavvio separato.
Procedura e limiti: [associazione e aggiornamenti](RELEASE_PAIRING_UX_2026-10-21.md).

## Correzione aggiornamenti Driver - e-Control 0.1.670-dist1

Aggiornare e-Control per avere **Aggiorna Driver** direttamente nella scheda
dell'elenco e distinguere gli aggiornamenti EKONEX dalle migrazioni HACS.
Corretta anche la verifica delle nuove versioni rispetto al catalogo Installer.
Per Dahua Access Reader 4.0.0 servono Installer53 ed e-Control670;
nessun aggiornamento Driver parte automaticamente.
Seguire la [procedura corretta](RELEASE_DRIVER_UPDATE_UI_2026-10-21.md).

## Dahua Access Reader 4.0.0 - 21 ottobre 2026

Installer `0.1.0-test53` rende disponibile il Driver Dahua Access Reader
`4.0.0`, aggiornamento di prova senza nuove funzioni. Aggiornare prima
l'App Installer, poi aprire il dettaglio del Driver e premere **Aggiorna Driver**.
Backup e consenso sono obbligatori; il riavvio di Home Assistant Core
richiede una conferma separata. Nessun aggiornamento Driver parte automaticamente.
Vedere la [procedura completa](RELEASE_DAHUA_ACCESS_4_2026-10-21.md).

## Aggiornamento Alexa - 21 ottobre 2026

e-Face `2.21.390-dist1` e Installer `0.1.0-test52`: correzione packaging
ownership e riconoscimento della variante Alexa legacy con fine riga Windows. Seguire la
[procedura manuale](RELEASE_ALEXA_2026-10-21.md); nessuna migrazione automatica.
Le note delle versioni precedenti sotto restano come storico.

Catalogo Home Assistant Ekonex, architettura amd64.
Codice e pacchetti dei prodotti restano privati. L'unico codice eseguibile pubblico
e il piccolo bootstrap ekonex_setup.

## Credenziali e Installer

1. Installa **Ekonex Installer - Avvio0.1.0-test10**: non richiede GHCR preconfigurato.
2. Segui la guida token classic read:packages; verifica e conferma il salvataggio.
   Il rinnovo di un registro esistente richiede conferma separata.
3. Avvio installa automaticamente **Ekonex Installer0.1.0-test8** se assente.
   Non aggiorna o reinstalla copie presenti: per queste usa la scheda Installer.

## Migrazione banco

Installer test8: nome senza suffisso Test, etichetta Sperimentale conservata.
Impianto operativo non selezionabile; promemoria arresto app prima dell'analisi.
Slug e dati invariati: aggiornare, non disinstallare e non ripetere migrazioni concluse.

Avvio test9 corregge anche lo stop del bootstrap: uscita0 a operazioni concluse,
log con data e ora UTC. Non occorre reinserire token o ripetere migrazioni.

Test7 corregge la chiusura dell'Installer: Arresta termina con codice 0 quando
non ci sono lavori attivi. Log avvio/arresto con data e ora UTC. Nessun dato
migrato modificato; non ripetere una migrazione gia completata.

Test6 corregge l'attesa di installazioni gia concluse dal Supervisor. Per una
sessione Test5 interrotta prima della copia, con backup verificato, aggiorna il
solo Installer senza disinstallarlo e usa **Riprendi migrazione**. Le copie gia
installate non sono reinstallate; originali, opzioni e backup sono ricontrollati.
La ripresa non parte automaticamente e non viene permessa dopo modifiche ai dati.

Installer Test6 abilita il collaudo banco e-Control/eFace/e-Safe con verifica
dei formati dati storici, senza liste chiuse di versioni. Include e-Control0.1.469
ed eFace2.21.328. Restano esclusi downgrade e formati non riconosciuti;
la selezione non attesta da sola la compatibilita. Vedi la [guida](ekonex_installer/DOCS.md).
Backup nativo verificato,
installazione delle copie mancanti, trasferimento dati e ripristino.
Richiede manutenzione temporanea del solo Installer: protezione disattivata
e riavvio prima della verifica prerequisiti, da riattivare dopo il collaudo.
Nessuna migrazione parte senza conferma. Nessuna copia viene avviata e nessun
originale viene eliminato. Altri prodotti e impianti operativi non abilitati.

Il successo dei test sintetici/Linux non sostituisce il collaudo sull'impianto
e sulle periferiche reali. Custodisci i backup locali come dati sensibili.

Aggiungere il catalogo non migra le vecchie installazioni. Le release dist1/dist2
dei nove prodotti identificano revisioni di distribuzione. Non sono stati
modificati i loro manifest, runtime o contratti per questa release Installer.
