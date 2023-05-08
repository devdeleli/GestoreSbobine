from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
from tkcalendar import *
from uploader.UploadDrive import *
from uploader.funzioni import *
import os

# Define variables



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
    root.geometry("750x500")
    center_window(root)

    # setup top frame
    top_frame = Frame(root)
    top_frame.pack(side=TOP, pady=10)

    # setup image and button for "Anatomia"
    anatomia_img = Image.open('./Media/Anatomia.png')
    anatomia_img = anatomia_img.resize((100, 100), Image.ANTIALIAS)
    anatomia_img = ImageTk.PhotoImage(anatomia_img)

    anatomia_button = Button(top_frame, image=anatomia_img, text='Anatomia', compound='bottom', width=100,
                             command=lambda: set_materia_anatomia())
    anatomia_button.pack(side=LEFT, padx=10)

    # setup image and button for "Fisiologia"
    fisiologia_img = Image.open('./Media/Fisiologia.png')
    fisiologia_img = fisiologia_img.resize((100, 100), Image.ANTIALIAS)
    fisiologia_img = ImageTk.PhotoImage(fisiologia_img)

    fisiologia_button = Button(top_frame, image=fisiologia_img, text='Fisiologia', compound='bottom', width=100,
                               command=lambda: set_materia_fisiologia())
    fisiologia_button.pack(side=LEFT, padx=10)

    materia_label= Label(top_frame, text=f'Materia Selezionata: Nessuna')
    materia_label.pack(side=LEFT, padx=10)




    # setup middle frame
    middle_frame = Frame(root)
    middle_frame.pack(side=TOP, pady=10)

    # setup date picker using tkcalendar
    date_label = Label(middle_frame, text='Data:')
    date_label.pack(side=LEFT, padx=10)

    cal = Calendar(middle_frame, selectmode='day', date_pattern='dd/MM/yyyy')
    cal.pack(side=LEFT)

    # setup text entry for description
    description_label = Label(middle_frame, text='Argomento: ')
    description_label.pack(side=LEFT, padx=10)

    description_entry = Entry(middle_frame, width=50)
    description_entry.pack(side=LEFT)

    # setup file selector
    file_label = Label(root, text='Seleziona il file:')
    file_label.pack(side=TOP, pady=10)

    file_button = Button(root, text='Scegli il file', command=lambda: choose_file())
    file_button.pack(side=TOP)

    # setup submit button
    submit_button = Button(root, text='Invia la Sbobina', command=upload_pdf_to_drive(select_file(), "1QQiyUMkPm3Z-kwBS69zM6DV4svvdWHGU"))
    submit_button.pack(side=BOTTOM, pady=10)



    # start main loop
    root.mainloop()


# Set interval
splash_root.after(3000, main)

# Execute tkinter
mainloop()
