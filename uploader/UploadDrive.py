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
from __main__ import *
from uploader import invio



def preparazione():
    __main__.CopiaSbobi()
    __main__.Rinomina()
    time.sleep(5)
    invio.upload_file(SelettoreCartella(__main__.materia), __main__.file_selezionato, "./Secure/gestoresbobine-0b458d4cb2b6.json")
    print("FATTO")


def SelettoreCartella(materia:str):
    folder_id = ""
    if materia == "Anatomia":
        folder_id = "1biJ5Rvxf35mYOHenhRpFPsgMi4cWWUKl"
    elif materia == "Fisiologia":
        folder_id = "1_XqHRTtsEF2oYYesdH4lIItCp5J-scY7"
    else:
        print("ERROR!!!")
    return folder_id



