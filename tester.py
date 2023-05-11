import os
import tkinter as tk
from google.oauth2 import service_account
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from tkinter import filedialog

# Define the Google Drive folder ID where you want to upload the file
FOLDER_ID = "1biJ5Rvxf35mYOHenhRpFPsgMi4cWWUKl"

# Define the scopes for accessing Google Drive
SCOPES = ["https://www.googleapis.com/auth/drive.file"]

# Create the Tkinter application
root = tk.Tk()
root.title("Google Drive Uploader")

# Define the function to handle file upload
def upload_file():
    # Prompt user to select file to upload
    file_path = filedialog.askopenfilename()

    # Create the Google Drive API client object
    credentials = service_account.Credentials.from_service_account_file('Secure/Creds.json', scopes=SCOPES)
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

# Create the Upload button
upload_button = tk.Button(root, text="Upload", command=upload_file)
upload_button.pack(padx=10, pady=10)

# Run the Tkinter event loop
root.mainloop()
