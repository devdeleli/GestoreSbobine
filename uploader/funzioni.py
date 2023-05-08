from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
from tkcalendar import *
from uploader.UploadDrive import *
from uploader.funzioni import *
import os

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

materia = ''
data_selezionata = ''
testo_libero = ''
file_selezionato = ''

def set_materia_anatomia() -> materia:
    global materia
    global materia_label
    materia = 'anatomia'
    return materia
    #imposta etichetta materia
    materia_label.configure(text=f'Materia Selezionata: {materia}')



def set_materia_fisiologia() -> materia:
    global materia
    materia = 'fisiologia'
    return materia
    #imposta etichetta materia
    materia_label.configure(text=f'Materia Selezionata: {materia}')


def select_file() -> file_selezionato:
    global file_selezionato
    global file_path
    filetypes = (('PDF files', '*.pdf'), ('All files', '*.*'))
    file_path = filedialog.askopenfilename(title='Select a file', filetypes=filetypes)
    if file_path:
        file_selezionato = file_path