# Ekonex Apps

Catalogo Home Assistant Ekonex, architettura amd64.
Codice e pacchetti dei prodotti restano privati. L'unico codice eseguibile pubblico
e il piccolo bootstrap ekonex_setup.

## Credenziali e Installer

1. Installa **Ekonex Installer - Avvio0.1.0-test6**: non richiede GHCR preconfigurato.
2. Segui la guida token classic read:packages; verifica e conferma il salvataggio.
   Il rinnovo di un registro esistente richiede conferma separata.
3. Avvio installa automaticamente **Installer - Test0.1.0-test5** se assente.
   Non aggiorna o reinstalla copie presenti: per queste usa la scheda Installer.

## Migrazione banco

Installer Test5 abilita il collaudo banco e-Control/eFace/e-Safe con verifica
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
