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
Qualora fosse necessario richiedere assistenza, collegarsi su GitHub e aprire una issue, 
assegnando come tag "help wanted". Assicurarsi di dettagliare nel modo migliore possibile 
il problema riscontrato o la richiesta di aiuto, allegando eventuali screenshot.

### Installazione di Python
Per installare python, è sufficiente seguire la [guida ufficiale](https://www.python.org/downloads/).
È necessario inoltre selezionare l'opzione "Add Python 3.11 to PATH" durante l'installazione.
Ora, conviene scaricare anche [Visual Studio Code](https://code.visualstudio.com/), che è un editor di testo,
per la modifica dei file di configurazione, come vedremo tra poco. È possibile utilizzare anche altri editor,
come [PyCharm](https://www.jetbrains.com/pycharm/) usato da me, dipende dalle vostre preferenze.
In ogni caso, è necessario che l'editor di testo sia in grado di eseguire codice python, per cui è necessario
installare l'estensione "Python" (o equivalente) per VSCode (PyCharm ha già tutto incluso).

[![PyCharm](https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green)](https://www.jetbrains.com/pycharm/)
[![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)](https://code.visualstudio.com/)


### Genesi dei file necessari al funzionamento del software
Per il corretto funzionamento del software è necessario che il responsabile delle sbobine abbia a disposizione
una cartella di Google Drive condivisa con tutti i membri del corso, nella quale verranno inserite le sbobine,
e che sia in possesso di un account Google con i permessi di lettura e scrittura su tale cartella.
Inoltre, è necessario che il responsabile delle sbobine abbia a disposizione un account google personale
per la genesi della mail di servizio e relative credenziali nel file JSON.
1. Il responsabile si collega alla propria [Google Cloud Console](https://console.cloud.google.com/) ;
2. Crea un nuovo progetto, nominandolo come preferisce. Al termine, lo apre;
3. Nella barra di ricerca, cerca "Google Drive API" e seleziona il primo risultato sotto "Marketplace";
4. Clicca su "Installa" e poi "Gestisci";
5. Seleziona sulla sinistra la voce "Credenziali";
6. In "account di servizio", seleziona "Crea account di servizio";
7. Inserisci un nome a piacere, modificando, se necessario "ID account" (questo è molto importante, rappresenterà l'indirizzo mail di caricamento) e clicca su "Crea";
8. Seleziona il ruolo "Project -> Proprietario" e clicca su "Continua";
9. Seleziona "Fine" in basso per creare l'account;
10. Seleziona la mail appena creata, clicca su "chiave" e poi su "Aggiungi chiave" - "Crea nuova chiave" - JSON;
11. Salva la chiave JSON in una cartella a piacere (per ora);
12. In ultimo, deve recarsi nella cartella Drive delle sbobine (meglio se nella directory principale, qualora
ci dovessero essere più sottocartelle per le diverse materie) e condividere la cartella con l'account appena creato,
semplicemente cliccando su "condivici", inserendo l'indirizzo mail e selezionando "editor" come permessi (deseleziona
"invia una notifica").

### Configurazione del software da parte del responsabile delle sbobine
Come prima cosa, deve importare il presente repository in locale, cliccando su "Code" e poi "Download ZIP".
Una volta scaricato, estraete il contenuto in una cartella a piacere (per semplicità, chiamiamola "GestoreSbobine").
Ora, aprite Visual Studio Code e cliccate su "File" - "Apri cartella" e selezionate la cartella appena creata.
A questo punto, entriamo nel vivo della configurazione:
1. Installiamo le dipendenze necessarie, aprendo il terminale di Visual Studio Code (Ctrl + Shift + ù) e digitando:
```pip install -r requirements.txt```. Qualora non dovesse funzionare, è necessario installare singolarmente
le dipendenze:

```shell
pip install google-api-python-client
pip install google-auth-httplib2
pip install google-auth-oauthlib
pip install google-auth
pip install google-api-core
pip install googleapis-common-protos
pip install pandas
pip install Pillow
pip install protobuf
pip install Requests
pip install tkcalendar
```
2. Copiamo nella cartella **./Secure/** il file JSON contenente le credenziali del servizio appena creato, e rinominiamolo in **Creds.JSON**;
3. Nella cartella **./Media/** carica le icone in formato PNG riguardanti le materie da sbobinare;
4. Rinomina il file **./Secure/ValoriBAK.JSON** in **./Secure/Valori.JSON** e modifica i valori in base alle tue esigenze, come mostrato nello snippet sottostante.
N.B.: allo stato attuale NON è possibile inserire in app più di 4 materie.
5. Esegui un caricamento di prova, per assicurarti che tutto funzioni correttamente. Puoi avviare l'applicazione 
facendo click con il tasto destro su **./__main__.py**;
6. Se tutto funziona correttamente, puoi generare il file da distribuire, seguendo le istruzioni di seguito.

#### Modifica del file Valori.JSON
Puoi modificare i valori come segue, avendo cura, qualora non dovessi utilizzare tutti i pulsanti, di
NON eliminare i valori non utilizzati, ma di impostare i campi come visto nell'esempio di "Materia1":
```json
{
    "Materia0_Nome":"Inserisci la materia",
    "Materia0_Img":"Inserisci il path completo ./Media/immagine.png",
    "Materia0_Fid":"inserisci l'id della cartella drive"
},
{
    "Materia1_Nome":"Non Attivo",
    "Materia1_Img":"./Media/None.png",
    "Materia1_Fid":"NULL"
}
```
Per quanto riguarda il Fid (Folder ID) può essere estratto nel seguente modo: vedendo il link che si trova
nella barra di ricerca del browser, estraiamo l'ultima stringa (drive.google.com/drive/folders/{Folder_ID}).
In pratica, recandosi su Google Drive e selezionando la cartella condivisa contenente le sbobine, 
copiare l'ultima parte dell'url. Per esempio, se l'URL è: drive.google.com/drive/folders/ABCDEF, l'ID è ABCDEF.

### Generazione dei file da distribuire ai colleghi

Le strade sono principalmente due:
1. Distribuzione del sorgente modificato;
2. Compilazione in eseguibile.

La prima strada, sebbene garantisca il corretto funzionamento nella totalità dei casi, risulta più complessa,
in quanto è necessario installare Python e relative dipendenze del software in ogni dispositivo su cui verrà 
utilizzato il GestoreSbobine. Cercheremo quindi di generare un eseguibile per le piattaforme, per semplificarne 
l'utilizzo. Ad ogni modo, verrà trattato alla fine come configurare i singoli dispositivi per l'utilizzo diretto 
del sorgente (in pratica, i passaggi **1** e **3** della configurazione).

#### Piattaforma Windows 
![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)
Allo stato attuale dei fatti (e delle mie conoscenze) risulta possibile elaborare solamente un file
eseguibile per la piattaforma Windows. Per farlo, è necessario installare il plugin Nuitka, che
permette di compilare il sorgente in un eseguibile, e "winrar", seguendo poi una serie di passaggi, qui
spiegati passo - passo:

**FASE PRELIMINARE**

1. Aprire il menù start e cercare "Python". Si aprirà una schermata simile al prompt dei comandi,
con scritto in alto "Python 3.XX;
2. Digitare il seguente comando: ```import googleapiclient``` e premere invio; 
3. Digitare ora ```print(googleapiclient.__file__)``` e premere invio. Comparirà una lunga stringa di testo: copiala;
4. Incollare la stringa appena copiata all'interno di esplora file, rimuovendo la parte terminale "googleapiclient/__init__.py";
5. Copiare la cartella "googleapiclient" sul desktop, aprendola al termine;
6. Eliminare tutti i file e le cartelle presenti, ad eccezione di "discovery_cache", "_auth.py", "_helpers.py" e "discovery.py";
7. Recarsi nella cartella "discovery_cache" ed eliminare tutti i file, ad eccezione di quelli che fanno riferimento a "drive" (sono 5 in tutto);

**"Conversione" in EXE**

8. Aprire il terminale di Visual Studio Code (Ctrl + Shift + ù) o di PyCharm e digitare:
```pip install nuitka```;
9. Aprire il file "ComandoNuitka.txt" predisposto e modificarlo secondo le indicazioni presenti. In particolare:
   - Inserire il percorso COMPLETO della cartella "Media";
   - Inserire il percorso COMPLETO della cartella "Secure";
   - Inserire il percorso COMPLETO della cartella "TEMP";
10. Copiare il comando appena modificato ed eseguirlo all'interno della console di Visual Studio Code (Ctrl + Shift + ù);
11. Se tutto è andato a buon fine, nella cartella "GestoreSbobine" verrà creata una cartella "__main__.dist", contenente
    il file eseguibile;
12. Copiare tutta la cartella "googleapiclient" dentro la cartella "__main__.dist";
13. Aprire la cartella "__main__.dist" e selezionare tutti i file, poi tasto destro, "aggiungi ad un archivio...";
14. Sotto "Metodo di compressione" selezionare "Migliore", poi spuntare "Crea un archivio auto-estraente";
15. Recarsi su "Avanzate", selezionare "Modulo auto-estraente", "Installa/Configura" e digitare sotto "Esegui dopo l'estrazione"
il comando "__main__.exe", senza virgolette;
16. Sotto "Modalità", selezionare "Estrai in una cartella temporanea", "Nascondi Tutto", mentre sotto "Aggiornamento", "Sovrascrivi tutti i file"
17. Adesso possiamo premere "OK" ed attendere la generazione del file "EXE", che sarà poi distribuito ai colleghi.

**N.B.: Alcuni antivirus (Kaspersky, Microsoft Defender...) possono riportare dei falsi positivi**

### Condivisione del sorgente (metodo NON consigliato)
Per tutti gli altri sistemi operativi, rimane possibile la condivisione del file sorgente appena elaborato.
Bisogna però preparare i computer all'esecuzione, seguendo i seguenti passaggi:
1. Installare Python 3.9.6 (o superiore) dal sito ufficiale;
2. Installare le dipendenze necessarie, aprendo il terminale di Visual Studio Code (Ctrl + Shift + ù) e digitando:
```pip install -r requirements.txt```. Qualora non dovesse funzionare, è necessario installarle singolarmente
   (si rimanda al punto **1** della guida per il responsabile);
3. Importare la cartella contenente il sorgente in Visual Studio Code (o PyCharm), cliccando su "File" - "Apri cartella" e selezionando la cartella appena creata;
4. Eseguire il file **./__main__.py**.

Sono consapevole che ciò non sia la via più rapida o più pratica, ma è l'unica che ho trovato per il momento.
Qualora qualcuno avesse suggerimenti, sono ben accetti, così come qualsiasi altro tipo di contributo.


## Contribuire
Per contribuire al progetto, è necessario seguire le seguenti istruzioni:
1. Eseguire il fork del progetto;
2. Creare un branch con il proprio nome;
3. Effettuare le modifiche;
4. Creare una pull request;
5. Attendere la revisione;
6. Se approvata, verrà effettuato il merge.


## To - Do
- [ ] Inserimento loading image...
- [ ] Inserimento pagina SETTING
- [ ] Caricamento Creds.JSON
- [ ] Modifica di cartelle dalla pagina SETTING
