# Import Module
from tkinter import *
import subprocess

# create root window
root = Tk()

programs = ["animations/bloody yin yang.py", "animations/solar system.py", "animations/dvd.py"]

# root window title and dimension
root.title("Quail Hub")
resolution = [800, 600]
root.geometry(f"{resolution[0]}x{resolution[1]}")

def clicked():
    process = subprocess.Popen(['python3', programs[0]])

def click2():
    process = subprocess.Popen(['python3', programs[1]])

def click3():
    process = subprocess.Popen(['python3', programs[2]])

lbl = Label(root, text = "Bloody Yin-Yang")
lbl.grid(column = 0, row = 0)
btn = Button(root, text = "Start" ,
             fg = "red", command=clicked)
btn.grid(column=2, row=0)

lbl = Label(root, text = "Space")
lbl.grid(column = 0, row = 1)
btn = Button(root, text = "Start" ,
             fg = "red", command=click2)
btn.grid(column=2, row=1)

lbl = Label(root, text = "DVD")
lbl.grid(column = 0, row = 2)
btn = Button(root, text = "Start" ,
             fg = "red", command=click3)
btn.grid(column=2, row=2)

# Execute Tkinter
root.mainloop()