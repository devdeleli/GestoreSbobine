from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog
from tkcalendar import *
from uploader.Send2Drive import *
from uploader.funzioni import *
import webbrowser
import os
import __main__

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))


def set_materia(materia:str,materia_label):
    '''
    Questa funzione permette di impostare la materia della sbobina
    :param materia: stringa che indica la materia
    :param materia_label: label che indica la materia selezionata (TKinter)
    :return:
    '''
    #materia = 'Anatomia'
    print(f"Caricherò la sbobina nella cartella {materia}")
    materia_label.configure(text=f'Materia Selezionata: {materia}')


global file_path
file_path = ""

def select_file():
    '''
    Questa funzione permette all'utente di selezionare il file da caricare
    :return:
    '''
    filetypes = (('PDF files', '*.pdf'), ('All files', '*.*'))
    file_path = filedialog.askopenfilename(title='Select a file', filetypes=filetypes)
    if file_path:
        __main__.filename_var.set(file_path)
    print(file_path)
    return file_path


def CopiaSbobi():
    '''
    Questa funzione copia il file selezionato dall'utente nella cartella TEMP
    :return: nome del file copiato (per funzione di rinomina)
    '''
    print("Sto copiando la sbobina...")
    file_path = __main__.filename_var.get()
    nome_file = os.path.basename(file_path)
    shutil.copy(file_path, "./TEMP/")
    return nome_file


def Rinomina():
    '''
    Questa funzione prende i dati inseriti dall'utente e rinomina il file copiato nella cartella TEMP
    '''
    numero_sbobina = __main__.numero_entry.get()
    giorno_sbobina = __main__.giorno_entry.get()
    mese_sbobina = __main__.mese_entry.get()
    mese_sbobina = mese_sbobina.title()
    argomento_sbobina = __main__.argomento_entry.get()
    argomento_maiusc = argomento_sbobina.title()
    argomento_maiusc = argomento_maiusc.replace(" ", "")
    nome_file = CopiaSbobi()
    nuovo_nome = numero_sbobina + "." + giorno_sbobina + mese_sbobina + " - " + argomento_maiusc + ".pdf"
    old_name = "./TEMP/" + nome_file
    new_name = "./TEMP/" + nuovo_nome
    print(f"Sto rinominando la sbobina in {nuovo_nome}...")
    os.rename(old_name, new_name)

def apri_finestra():
    InfoSoftware = tk.Toplevel()
    InfoSoftware.title("Info sul Software")
    InfoSoftware.geometry("500x250")
    center_window(InfoSoftware)

    info_label = Label(InfoSoftware, text="Lecture Transcript Online Update System \n "
                                      "Developed by DEVDELELI: \n "
                                      "https://www.github.com/devdeleli",
                       anchor=CENTER, font=("Helvetica", 12))
    info_label.pack(side=TOP, padx=10, pady=50, anchor="center")
    info_label.bind("<Button-1>", lambda e:
                    webbrowser.open_new_tab("https://www.github.com/devdeleli"))




