from tkinter import *
from PIL import Image, ImageTk

splash_root = Tk()
splash_root.overrideredirect(True)

# get screen width and height
screen_width = splash_root.winfo_screenwidth()
screen_height = splash_root.winfo_screenheight()

# set window size and position
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
    # destroy splash window
    splash_root.destroy()

    # Execute tkinter
    root = Tk()

    # Adjust size
    root.geometry("400x400")

    # Add your widgets here

# Set Interval
splash_root.after(3000, main)

# Execute tkinter
mainloop()
