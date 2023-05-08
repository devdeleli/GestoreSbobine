from tkinter import *
from PIL import Image, ImageTk
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from tkinter import filedialog
from uploader.UploadDrive import upload_pdf_to_drive
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




# Set interval
splash_root.after(3000, main)

# Execute tkinter
mainloop()
