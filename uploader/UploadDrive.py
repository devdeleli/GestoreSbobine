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


def SelettoreCartella():
    print("SelettoreCartella")


def RimuoviSbobina():
    print("RimuoviSbobina")










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