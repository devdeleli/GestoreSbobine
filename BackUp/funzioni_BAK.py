from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
from tkcalendar import *
from uploader.UploadDrive import *
from uploader.funzioni import *
import os
import __main__
def choose_file():
    file_path = filedialog.askopenfilename(initialdir='/', title='Scegli un file',
                                           filetypes=(('PDF files', '*.pdf'), ('all files', '*.*')))


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


def on_date_selected(event, cal):
    data_selezionata = cal.get_date()
    print(data_selezionata)



def set_materia_fisiologia(materia,materia_label):
    materia = 'Fisiologia'
    print(materia)
    materia_label.configure(text=f'Materia Selezionata: {materia}')
    return materia


global file_path
file_path = ""

def select_file() -> str:
    filetypes = (('PDF files', '*.pdf'), ('All files', '*.*'))
    file_path = filedialog.askopenfilename(title='Select a file', filetypes=filetypes)
    file_path = __main__.filename_var
    return file_path



def get_filepath() -> str:
    return file_path


