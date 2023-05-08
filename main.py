from tkinter import *
from PIL import Image, ImageTk
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from tkinter import filedialog
from uploader.UploadDrive import upload_pdf_to_drive
from datetime import datetime
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

# Define variables
materia = ''
data_selezionata = ''
testo_libero = ''
file_selezionato = ''

# Define functions
def set_materia_anatomia():
    global materia
    materia = 'anatomia'

def set_materia_fisiologia():
    global materia
    materia = 'fisiologia'

def select_file():
    global file_selezionato
    filetypes = (('PDF files', '*.pdf'), ('All files', '*.*'))
    file_path = filedialog.askopenfilename(title='Select a file', filetypes=filetypes)
    if file_path:
        file_selezionato = file_path

def invia_sbobina():
    global data_selezionata, testo_libero, file_selezionato, materia
    print(f"Materia selezionata: {materia}")
    print(f"Data selezionata: {data_selezionata}")
    print(f"Testo libero: {testo_libero}")
    print(f"File selezionato: {file_selezionato}")

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

    top_frame = Frame(root)
    top_frame.pack(side=TOP, pady=20)

    img = Image.open("./Media/Anatomia.png").resize((50, 50))
    photo_img_anat = ImageTk.PhotoImage(img)
    anatomia_button = Button(top_frame, image=photo_img_anat, text='Anatomia', compound='bottom',
                             command=set_materia_anatomia, width=100, height=100)
    anatomia_button.pack(side=LEFT, padx=50)

    img = Image.open("./Media/Fisiologia.png").resize((50, 50))
    photo_img_fisio = ImageTk.PhotoImage(img)
    fisiologia_button = Button(top_frame, image=photo_img_fisio, text='Fisiologia', compound='bottom',
                               command=set_materia_fisiologia, width=100, height=100)
    fisiologia_button.pack(side=LEFT, padx=50)

    # Create middle frame with date and text inputs
    middle_frame = Frame(root)
    middle_frame.pack(side=TOP, pady=20)

    now = datetime.now()
    current_date = now.strftime('%d %B')
    date_label = Label(middle_frame, text=current_date)
    date_label.pack(side=LEFT, padx=50)

    testo_label = Label(middle_frame, text='Testo Libero:')
    testo_label.pack(side=LEFT, padx=50)
    testo_entry = Entry(middle_frame, width=30)
    testo_entry.pack(side=LEFT)

    # Create bottom frame with file selection and send button
    bottom_frame = Frame(root)
    bottom_frame.pack(side=TOP, pady=20)

    file_button = Button(bottom_frame, text='Seleziona un File', command=select_file)
    file_button.pack(side=LEFT, padx=50)

    invia_button = Button(bottom_frame, text='Invia la Sbobina', command=invia_sbobina)
    invia_button.pack(side=LEFT, padx=50)




# Set interval
splash_root.after(3000, main)

# Execute tkinter
mainloop()
