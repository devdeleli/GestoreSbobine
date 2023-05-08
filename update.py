import os
import pickle
import google.auth
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

# Imposta il percorso del file delle credenziali API
creds_path = './Secure/gestoresbobine-0b458d4cb2b6.json'

# Verifica se le credenziali esistono
if not os.path.exists(creds_path):
    print("Il file delle credenziali API non esiste")
else:
    # Autenticati con le credenziali API
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = google.auth.load_credentials_from_file(creds_path, scopes=['https://www.googleapis.com/auth/drive'])
            creds = flow[0]
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    # Crea l'oggetto per interagire con l'API di Google Drive
    drive_service = build('drive', 'v3', credentials=creds)

    # Imposta il percorso del file da caricare
    file_path = 'path/to/your/file'

    # Imposta il nome della cartella in cui caricare il file
    folder_name = 'Nome cartella'

    # Cerca la cartella per nome
    folder_query = "mimeType='application/vnd.google-apps.folder' and trashed = false and name = '{}'".format(folder_name)
    folder_results = drive_service.files().list(q=folder_query,fields="nextPageToken, files(id, name)").execute()
    folder_items = folder_results.get('files', [])
    if not folder_items:
        print("Nessuna cartella trovata con il nome '{}'".format(folder_name))
    else:
        folder_id = folder_items[0]['id']

        # Carica il file nella cartella
        file_metadata = {'name': os.path.basename(file_path), 'parents': [folder_id]}
        media = MediaFileUpload(file_path, resumable=True)
        file = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        print("File caricato con successo con ID: {}".format(file.get('id')))
