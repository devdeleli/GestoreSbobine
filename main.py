from tkinter import *
from PIL import Image, ImageTk
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from tkinter import filedialog
import os

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

def UploadAnatomia():
    print("ok")

def UploadFisiologia():
    print("OK")


# Google Drive API credentials file path
creds_path = './Secure/gestoresbobine-0b458d4cb2b6.json'

# Google Drive API v3 scope for file access and modification
scope = ['https://www.googleapis.com/auth/drive.file']

# Create credentials object from credentials file and scope
creds = service_account.Credentials.from_service_account_file(creds_path, scopes=scope)


# Define function to handle file upload to Google Drive
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


# Create the splash screen window
splash_root = Tk()
splash_root.overrideredirect(True)

# Get screen width and height
screen_width = splash_root.winfo_screenwidth()
screen_height = splash_root.winfo_screenheight()

# Set window size and position
splash_width = 750
splash_height = 500
x_pos = (screen_width // 2) - (splash_width // 2)
y_pos = (screen_height // 2) - (splash_height // 2)
splash_root.geometry(f"{splash_width}x{splash_height}+{x_pos}+{y_pos}")

# Create a PhotoImage object from your image
img = PhotoImage(file="./Media/Splash.png")

# Create a label with the image
splash_label = Label(splash_root, image=img)
splash_label.pack()


def main():
    # Destroy splash window
    splash_root.destroy()

    # Execute tkinter
    root = Tk()

    # Adjust size
    root.geometry("750x500")
    center_window(root)

    # Add your widgets here
    btn_upload = Button(root, text="Upload PDF to Google Drive", command=upload_pdf_to_drive)
    btn_upload.pack(pady=20)

    img1 = ImageTk.PhotoImage(Image.open("./Media/button1.png"))
    button1 = Button(frame, image=img1, text="Button 1", compound="bottom", command=button1_click, bd=0,
                     highlightthickness=0)
    button1.image = img1
    button1.pack(side="left", padx=10, pady=10)

    # create the second button
    img2 = ImageTk.PhotoImage(Image.open("./Media/button2.png"))
    button2 = Button(frame, image=img2, text="Button 2", compound="bottom", command=button2_click, bd=0,
                     highlightthickness=0)
    button2.image = img2
    button2.pack(side="left", padx=10, pady=10)


# Set interval
splash_root.after(3000, main)

# Execute tkinter
mainloop()
