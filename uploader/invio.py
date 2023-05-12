#from google.oauth2.credentials import Credentials
from google.oauth2 import service_account
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import os

def upload_file(file_PTH:str, FLDR_2_UP:str, cred:str):
    # Prompt user to select file to upload
    SCOPES = ["https://www.googleapis.com/auth/drive.file"]
    file_path = file_PTH
    FOLDER_ID = FLDR_2_UP

    # Create the Google Drive API client object
    credentials = service_account.Credentials.from_service_account_file(cred, scopes=SCOPES)
    service = build('drive', 'v3', credentials=credentials)

    # Set the metadata for the new file
    file_metadata = {
        'name': os.path.basename(file_path),
        'parents': [FOLDER_ID]
    }

    # Upload the file to Google Drive
    try:
        media = MediaFileUpload(file_path)
        file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        print(f"File ID: {file.get('id')} - '{file.get('name')}' has been uploaded to Google Drive.")
    except HttpError as error:
        print(f"An error occurred: {error}")
        file = None