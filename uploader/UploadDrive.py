import time
from tkinter import *
from PIL import Image, ImageTk
from google.oauth2 import service_account
from google.oauth2.service_account import Credentials
from google.oauth2 import service_account
import json
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


with open('./Secure/Valori.JSON') as f:
    data = json.load(f)


def esegui_upload(SBJ):
    uploader.funzioni.CopiaSbobi()
    uploader.funzioni.Rinomina()
    time.sleep(5)
    invio.upload_file(select_pdf_file("./TEMP/"), SelettoreCartellaDrive(SBJ), "./Secure/Creds.json")
    time.sleep(5)
    delete_all_pdf_files("./TEMP/")
    time.sleep(3)
    print("La sbobina è stata correttamente caricata")


def SelettoreCartellaDrive(subject:str):
    '''
    Questa funzione permette di selezionare la cartella in cui caricare il file
    :param subject: Indica la materia della sbobina
    :return:
    '''
    SubjectLabel = subject.cget("text")
    subject_rec = SubjectLabel.split(": ", 1)[1]
    with open(os.path.abspath('Secure/Valori.JSON')) as f:
        data = json.load(f)
    folder_id = ""
    if subject_rec == data[0]["Materia0_Nome"]:
        folder_id = data[0]["Materia0_Fid"]
    elif subject_rec == data[1]["Materia1_Nome"]:
        folder_id = data[1]["Materia1_Fid"]
    elif subject_rec == data[2]["Materia2_Nome"]:
        folder_id = data[2]["Materia2_Fid"]
    elif subject_rec == data[3]["Materia3_Nome"]:
        folder_id = data[3]["Materia3_Fid"]
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
    print("Il file è stato selezionato ed è pronto per l'invio")

def delete_all_pdf_files(folder_path):
    '''
    Questa funzione permette di eliminare tutti i file pdf presenti nella cartella folder_path
    :param folder_path:
    '''
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.pdf'):
            os.remove(os.path.join(folder_path, file_name))
    print("La procedura di trasferimento è stata completata correttamente")