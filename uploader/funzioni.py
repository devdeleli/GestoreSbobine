from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
from tkcalendar import *
from uploader.UploadDrive import *
from uploader.funzioni import *
import os
import __main__



def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))



def set_materia_anatomia(materia,materia_label):
    materia = 'Anatomia'
    print(materia)
    materia_label.configure(text=f'Materia Selezionata: {materia}')
    return materia


def on_date_selected(event, cal) -> str:
    global dataselezionata
    dataselezionata = cal.get_date()
    print(dataselezionata)
    return dataselezionata


def validate_input(new_value):
    return new_value.isnumeric() or new_value == ""



def set_materia_fisiologia(materia,materia_label):
    materia = 'Fisiologia'
    print(materia)
    materia_label.configure(text=f'Materia Selezionata: {materia}')
    return materia


global file_path
file_path = ""

def select_file():
    filetypes = (('PDF files', '*.pdf'), ('All files', '*.*'))
    file_path = filedialog.askopenfilename(title='Select a file', filetypes=filetypes)
    if file_path:
        __main__.filename_var.set(file_path)
    return file_path




def get_filepath() -> str:
    return file_path


