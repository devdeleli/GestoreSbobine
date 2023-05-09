from google.oauth2.credentials import Credentials
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
import os

def upload_file(folder_id: str, file_path: str, credentials_path: str):
    # Create the Google Drive API client object
    credentials = Credentials.from_service_account_file(credentials_path, scopes=['https://www.googleapis.com/auth/drive'])
    service = build('drive', 'v3', credentials=credentials)

    # Set the metadata for the new file
    file_metadata = {
        'name': os.path.basename(file_path),
        'parents': [folder_id]
    }

    # Upload the file to Google Drive
    try:
        media = MediaFileUpload(file_path)
        file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        print(f"File ID: {file.get('id')} - '{file.get('name')}' has been uploaded to Google Drive.")
    except HttpError as error:
        print(f"An error occurred: {error}")
        file = None
