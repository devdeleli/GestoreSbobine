import __main__
from uploader.UploadDrive import *
from uploader.funzioni import *
import os

global nome_file
numero_entry = ""
giorno_entry = ""
mese_entry = ""
argomento_entry = ""
nuovo_nome = ""


# Define variables
global materia
materia = 'Nessuna'
dataselezionata = ''
testo_libero = ''
file_selezionato = ''
folder_id = ""


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

    # Adjust size
    root.geometry("750x550")
    center_window(root)

    # setup top frame
    top_frame = Frame(root)
    top_frame.pack(side=TOP, pady=10)

    # setup image and button for "Anatomia"
    anatomia_img = Image.open('./Media/Anatomia.png')
    anatomia_img = anatomia_img.resize((100, 100))
    anatomia_img = ImageTk.PhotoImage(anatomia_img)

    anatomia_button = Button(top_frame, image=anatomia_img, text='Anatomia', compound='bottom', width=100,
                             command=lambda: set_materia("Anatomia",materia_label))
    anatomia_button.pack(side=LEFT, padx=10)

    # setup image and button for "Fisiologia"
    fisiologia_img = Image.open('./Media/Fisiologia.png')
    fisiologia_img = fisiologia_img.resize((100, 100))
    fisiologia_img = ImageTk.PhotoImage(fisiologia_img)

    fisiologia_button = Button(top_frame, image=fisiologia_img, text='Fisiologia', compound='bottom', width=100,
                               command=lambda: set_materia("Fisiologia",materia_label))
    fisiologia_button.pack(side=LEFT, padx=10)

    materia_label= Label(top_frame, text=f'Materia Selezionata: {materia}')
    materia_label.pack(side=LEFT, padx=10)

    # setup middle frame
    middle_frame = Frame(root)
    middle_frame.pack(side=TOP, pady=10)

    # setup table
    table_frame = Frame(middle_frame)
    table_frame.pack(side=TOP)

    # setup image
    image_label = Label(table_frame, image= None)
    image_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

    # setup entries
    numero_label = Label(table_frame, text='Numero Sbobina:')
    numero_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)
    __main__.numero_entry = Entry(table_frame)
    numero_entry.grid(row=1, column=1, padx=10, pady=10)

    giorno_label = Label(table_frame, text='Giorno Sbobina:')
    giorno_label.grid(row=2, column=0, padx=10, pady=10, sticky=W)
    __main__.giorno_entry = Entry(table_frame)
    giorno_entry.grid(row=2, column=1, padx=10, pady=10)

    mese_label = Label(table_frame, text='Mese Sbobina:')
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

    # setup submit button
    submit_button = Button(middle_frame, text='Invia la Sbobina', command=lambda: preparazione())
    submit_button.pack(side=TOP, pady=10)

    # start main loop
    root.mainloop()


# Set interval
splash_root.after(500, main) #tempo in millisecondi di splash screen

# Execute tkinter
mainloop()
