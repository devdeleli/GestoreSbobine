from tkinter import *
from PIL import Image, ImageTk
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from tkinter import filedialog
import requests
import csv
import pandas as pd
import os
from __main__ import *

def download_CSV_nomi():
    url = "https://drive.google.com/uc?export=download&id=1DCfa8WTsaJrx9qSmV88nA2ZeZe8WxUHr"
    response = requests.get(url)

    if response.status_code == 200:
        filename = "Base_Nomi.csv"
        filepath = os.path.join("./TEMP/", filename)
        with open(filepath, "wb") as f:
            f.write(response.content)
            print(f"File {filename} salvato in {filepath}")
    else:
        print(f"Errore nella richiesta. Status code: {response.status_code}")


def find_primonome(data_selezionata) -> str:
    df = pd.read_csv("./TEMP/Base_Nomi.csv", sep=";")
    colonna_data = df.iloc[:, 0]
    indice_riga = colonna_data[colonna_data == data_selezionata].index.tolist()
    if indice_riga:
        primonome = df.iloc[indice_riga[0], 1]
    else:
        primonome = "Ciii"  # oppure un valore di default, se preferisci
    print(primonome)
    print(data_selezionata)
    return primonome

def preparazione():
    download_CSV_nomi()
    print("Download completato")
    print(find_primonome())




def upload_pdf_to_drive(filepath:str, folder_id:str):
    # Prompt user to select file to upload

    if not filepath:
        return

    # Set the folder ID of the destination folder on Google Drive
    folder_id = '1QQiyUMkPm3Z-kwBS69zM6DV4svvdWHGU'

    # Create the Google Drive API client object
    service = build('drive', 'v3', credentials=creds)

    # Set the metadata for the new file
    file_metadata = {
        'name': os.path.basename(filepath),
        'parents': [folder_id],
        'mimeType': 'application/pdf'
    }

    # Upload the file to Google Drive
    try:
        media = MediaFileUpload(filepath, mimetype='application/pdf')
        file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        print(f"File ID: {file.get('id')} - '{file.get('name')}' has been uploaded to Google Drive.")
    except HttpError as error:
        print(f"An error occurred: {error}")
        file = None