# GestoreSbobine


![GitHub](https://img.shields.io/github/license/devdeleli/Python_Code?label=license)
[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/release/python-3113/)

## Descrizione
Il presente software python serve a facilitare la catalogazione delle sbobine universitarie. 
Mediante un'interfaccia semplice ed intuitiva, l'utente può inserire i dati relativi alle sbobine,
oltre che selezionare il file PDF della stessa, che verrà rinominata in accordo con i dati inseriti e caricata 
nella cartella di Google Drive del corso. Per i dettagli sulla configurazione vedere oltre.

## Configurazione
La configurazione è divisa in quattro parti:
- Installazione di Python (solo responsabile delle sbobine)
- Genesi dei file necessari al funzionamento del software
- Configurazione del software da parte del responsabile delle sbobine
- Generazione del file .exe da distribuire

Analizzeremo nel dettaglio ogni punto.

### Installazione di Python
Per installare python, è sufficiente seguire la [guida ufficiale](https://www.python.org/downloads/).
È necessario inoltre selezionare l'opzione "Add Python 3.11 to PATH" durante l'installazione.
Ora, conviene scaricare anche [Visual Studio Code](https://code.visualstudio.com/), che è un editor di testo,
per la modifica dei file di configurazione, come vedremo tra poco.


### Genesi dei file necessari al funzionamento del software
Per il corretto funzionamento del software è necessario che il responsabile delle sbobine abbia a disposizione
una cartella di Google Drive condivisa con tutti i membri del corso, nella quale verranno inserite le sbobine,
e che sia in possesso di un account Google con i permessi di lettura e scrittura su tale cartella.
Inoltre, è necessario che il responsabile delle sbobine abbia a disposizione un account google personale
per la genesi della mail di servizio e relative credenziali nel file JSON.
1. Il responsabile si collega alla propria [Google Cloud Console](https://console.cloud.google.com/)
2. Crea un nuovo progetto, nominandolo come preferisce. Al termine, lo apre
3. Nella barra di ricerca, cerca "Google Drive API" e seleziona il primo risultato sotto "Marketplace"
4. Clicca su "Installa" e poi "Gestisci"
5. Seleziona sulla sinistra la voce "Credenziali"
6. In "account di servizio", seleziona "Crea account di servizio"
7. Inserisci un nome a piacere, modificando, se necessario "ID account" (questo è molto importante, rappresenterà l'indirizzo mail di caricamento) e clicca su "Crea"
8. Seleziona il ruolo "Project -> Proprietario" e clicca su "Continua"
9. Seleziona "Fine" in basso per creare l'account
10. Seleziona la mail appena creata, clicca su "chiave" e poi su "Aggiungi chiave" - "Crea nuova chiave" - JSON
11. Salva la chiave JSON in una cartella a piacere (per ora).

### Configurazione del software da parte del responsabile delle sbobine
Come prima cosa, deve importare il presente repository in locale, cliccando su "Code" e poi "Download ZIP".
Una volta scaricato, estraete il contenuto in una cartella a piacere (per semplicità, chiamiamola "GestoreSbobine").
Ora, aprite Visual Studio Code e cliccate su "File" - "Apri cartella" e selezionate la cartella appena creata.
A questo punto, entriamo nel vivo della configurazione:
1. Installiamo le dipendenze necessarie, aprendo il terminale di Visual Studio Code (Ctrl + Shift + ù) e digitando:
```pip install -r requirements.txt```
2. Copiamo nella cartella **./Secure/** il file JSON contenente le credenziali del servizio appena creato
3. to be continued...




### Generazione del file .exe da distribuire


## Utilizzo

