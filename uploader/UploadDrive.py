import time
from tkinter import *
from PIL import Image, ImageTk
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from tkinter import filedialog
import shutil
import requests
import csv
import pandas as pd
import os

import __main__
from __main__ import *




def Rinomina():
    print("Rinomina")


def RimuoviSbobina():
    print("RimuoviSbobina")





def preparazione():
    __main__.CopiaSbobi()
    time.sleep(5)
    upload_pdf_to_drive("./TEMP/1.11 - 1.pdf", "1biJ5Rvxf35mYOHenhRpFPsgMi4cWWUKl")
    __main__.RimuoviSbobina(__main__.nuovo_nome)

def SelettoreCartella(materia:str):
    folder_id = ""
    if materia == "Anatomia":
        folder_id = "1biJ5Rvxf35mYOHenhRpFPsgMi4cWWUKl"
    elif materia == "Fisiologia":
        folder_id = "1_XqHRTtsEF2oYYesdH4lIItCp5J-scY7"
    else:
        print("ERROR!!!")
    return folder_id



def upload_pdf_to_drive(filepath:str, folder_id:str):
    # Prompt user to select file to upload

    if not filepath:
        return

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