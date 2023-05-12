import  __main__
import uploader.Send2Drive
from uploader.Send2Drive import *
from uploader.Send2Drive import esegui_upload
from uploader.funzioni import *
import sys
import json
from tkinter.scrolledtext import ScrolledText
from itertools import count, cycle
from uploader.Classes import *

global nome_file
numero_entry = ""
giorno_entry = ""
mese_entry = ""
argomento_entry = ""
nuovo_nome = ""


# Define variables

materia = 'Nessuna'
dataselezionata = ''
testo_libero = ''
file_selezionato = ''
folder_id = ""

##########
with open('./Secure/Valori.JSON') as f:
    data = json.load(f)
##########

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
    root.title("Lecture Transcript Upload System")

    # Adjust Size
    root.geometry("750x700")
    center_window(root)

    # setup top frame
    top_frame = Frame(root)
    top_frame.pack(side=TOP, pady=10)

    # setup image and button for "Materia1"
    materia1 = Image.open(data[0]["Materia0_Img"])
    materia1 = materia1.resize((100, 100))
    materia1 = ImageTk.PhotoImage(materia1)

    materia1_button = Button(top_frame, image=materia1, text=data[0]["Materia0_Nome"], compound='bottom', width=100,
                             command=lambda: set_materia(data[0]["Materia0_Nome"], materia_label))
    materia1_button.grid(row=1, column=0, padx=10, pady=10, sticky=W)

    # setup image and button for "Materia2"
    materia2 = Image.open(data[1]["Materia1_Img"])
    materia2 = materia2.resize((100, 100))
    materia2 = ImageTk.PhotoImage(materia2)

    materia2_button = Button(top_frame, image=materia2, text=data[1]["Materia1_Nome"], compound='bottom', width=100,
                             command=lambda: set_materia(data[1]["Materia1_Nome"], materia_label))
    materia2_button.grid(row=1, column=1, padx=10, pady=10, sticky=W)

    # setup image and button for "Materia3"
    materia3 = Image.open(data[2]["Materia2_Img"])
    materia3 = materia3.resize((100, 100))
    materia3 = ImageTk.PhotoImage(materia3)

    materia3_button = Button(top_frame, image=materia3, text=data[2]["Materia2_Nome"], compound='bottom', width=100,
                             command=lambda: set_materia(data[2]["Materia2_Nome"], materia_label))
    materia3_button.grid(row=1, column=2, padx=10, pady=10, sticky=W)

    # setup image and button for "Materia4"
    materia4 = Image.open(data[3]["Materia3_Img"])
    materia4 = materia4.resize((100, 100))
    materia4 = ImageTk.PhotoImage(materia4)

    materia4_button = Button(top_frame, image=materia4, text=data[3]["Materia3_Nome"], compound='bottom', width=100,
                             command=lambda: set_materia(data[3]["Materia3_Nome"], materia_label))
    materia4_button.grid(row=1, column=3, padx=10, pady=10, sticky=W)

    materia_label = Label(top_frame, text=f'Materia Selezionata: {__main__.materia}')
    materia_label.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky=W)

    # setup middle frame
    middle_frame = Frame(root)
    middle_frame.pack(side=TOP, pady=10)

    # setup table
    table_frame = Frame(middle_frame)
    table_frame.pack(side=TOP)

    # setup entries
    numero_label = Label(table_frame, text='Numero Sbobina (Due cifre ##):')
    numero_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)
    __main__.numero_entry = Entry(table_frame)
    numero_entry.grid(row=1, column=1, padx=10, pady=10)

    giorno_label = Label(table_frame, text='Giorno Sbobina (Due cifre ##):')
    giorno_label.grid(row=2, column=0, padx=10, pady=10, sticky=W)
    __main__.giorno_entry = Entry(table_frame)
    giorno_entry.grid(row=2, column=1, padx=10, pady=10)

    mese_label = Label(table_frame, text='Mese Sbobina (letterale):')
    mese_label.grid(row=3, column=0, padx=10, pady=10, sticky=W)
    __main__.mese_entry = Entry(table_frame)
    mese_entry.grid(row=3, column=1, padx=10, pady=10)

    argomento_label = Label(table_frame, text='Argomento Sbobina:')
    argomento_label.grid(row=4, column=0, padx=10, pady=10, sticky=W)
    __main__.argomento_entry = Entry(table_frame)
    argomento_entry.grid(row=4, column=1, padx=10, pady=10)

    # setup file selector
    file_label = Label(middle_frame, text='Seleziona il file:')
    file_label.pack(side=TOP, pady=10)

    file_frame = Frame(middle_frame)
    file_frame.pack(side=TOP)

    global filename_var
    filename_var = StringVar()
    filename_var.set(file_path)

    file_entry = Entry(file_frame, textvariable=filename_var, width=70)
    file_entry.pack(side=RIGHT)

    file_button = Button(file_frame, text='Scegli il file', command=lambda: select_file())
    file_button.pack(side=RIGHT, padx=10)

    # setup button frame
    button_frame = Frame(middle_frame)
    button_frame.pack(side=TOP, pady=10)

    # setup submit button
    submit_button = Button(button_frame, text='Invia la Sbobina', command=lambda: esegui_upload(materia_label))
    submit_button.pack(side=LEFT, padx=10)

    # setup info button
    info_button = Button(button_frame, text='Info sul Software', command=lambda: apri_finestra())

    info_button.pack(side=LEFT, padx=10)

    # position button frame in center
    button_frame.pack(side=TOP, pady=10, anchor="center")

    # setup bottom frame
    bottom_frame = Frame(root)
    bottom_frame.pack(side=BOTTOM, pady=10)

    #### Terminal Output ####

    # setup terminal output
    output_label = Label(bottom_frame, text='Terminal Output:')
    output_label.pack(side=TOP, pady=5)

    output_text = ScrolledText(bottom_frame, width=80, height=10)
    output_text.pack(side=TOP, padx=10, pady=5)
    output_text.see(END)

    # redirect stdout to the Text widget
    sys.stdout = TextRedirector(output_text, "stdout")

    # redirect stderr to the Text widget
    sys.stderr = TextRedirector(output_text, "stderr")

    # start main loop
    root.mainloop()

# Set interval
splash_root.after(3000, main)  #tempo in millisecondi di splash screen

# Execute tkinter
mainloop()