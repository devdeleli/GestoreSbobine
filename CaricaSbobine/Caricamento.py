import os
import json
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Change the following two variables with your actual values
JSON_FILE_PATH = './Secure/gestoresbobine-c06cf245a114.json'
FOLDER_ID = 'your-folder-id'


def get_authenticated_service(api_name, api_version, scopes):
    """Authenticate and return the specified API service"""

    # Load the JSON file with your credentials
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', scopes)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            with open(JSON_FILE_PATH, 'r') as json_file:
                data = json.load(json_file)
                creds = Credentials.from_authorized_user_info(data)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    # Build and return the service object
    service = build(api_name, api_version, credentials=creds)
    return service


def upload_pdf_file(file_path, folder_id):
    """Upload a PDF file to the specified folder"""

    # Authenticate and get the Drive API service
    service = get_authenticated_service('drive', 'v3', ['https://www.googleapis.com/auth/drive'])

    # Create the metadata for the file
    file_metadata = {'name': os.path.basename(file_path), 'parents': [folder_id], 'mimeType': 'application/pdf'}

    # Create the MediaFileUpload object
    media = MediaFileUpload(file_path, mimetype='application/pdf', resumable=True)

    try:
        # Upload the file to Drive
        file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        print(f'File ID: {file.get("id")}')

    except HttpError as error:
        print(f'An error occurred: {error}')
        file = None

    return file
