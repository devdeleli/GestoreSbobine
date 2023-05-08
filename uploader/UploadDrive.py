from tkinter import *
from PIL import Image, ImageTk
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from tkinter import filedialog
import os

def upload_pdf_to_drive():
    # Prompt user to select file to upload
    filepath = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select a PDF file",
                                          filetypes=(("PDF files", "*.pdf"), ("all files", "*.*")))
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