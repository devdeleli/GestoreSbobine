import time
from tkinter import *
from PIL import Image, ImageTk
from google.oauth2 import service_account
from google.oauth2.service_account import Credentials
from google.oauth2 import service_account

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from tkinter import filedialog
import shutil
import requests
import csv
import pandas as pd
import os

import __main__
import uploader.funzioni
from __main__ import *
from uploader import invio



def preparazione():
    uploader.funzioni.CopiaSbobi()
    uploader.funzioni.Rinomina()
    time.sleep(5)
    invio.upload_file(select_pdf_file("./TEMP/"), "1biJ5Rvxf35mYOHenhRpFPsgMi4cWWUKl", "./Secure/gestoresbobine-0b458d4cb2b6.json")
    time.sleep(5)
    delete_all_pdf_files("./TEMP/")
    print("La sbobina è stata correttamente caricata")


def SelettoreCartella(materia:str): #non passa correttiamente la variabile. correggere
    folder_id = ""
    if materia == "Anatomia":
        folder_id = "1biJ5Rvxf35mYOHenhRpFPsgMi4cWWUKl"
    elif materia == "Fisiologia":
        folder_id = "1_XqHRTtsEF2oYYesdH4lIItCp5J-scY7"
    else:
        print("ERROR!!!")
    return folder_id

def select_pdf_file(directory):
    '''
    Questa funzione permette di selezionare il file pdf da caricare (supponendo che sia solo uno)
    :param directory:
    '''
    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            return os.path.join(directory, filename)

def delete_all_pdf_files(folder_path):
    '''
    Questa funzione permette di eliminare tutti i file pdf presenti nella cartella folder_path
    :param folder_path:
    '''
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.pdf'):
            os.remove(os.path.join(folder_path, file_name))
