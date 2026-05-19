# Import Module
from tkinter import *
import subprocess
import sys, os

# create root window
root = Tk()


# root window title and dimension
root.title("Quail Hub")
resolution = [800, 600]
root.geometry(f"{resolution[0]}x{resolution[1]}")

def run_program(name):
    os.chdir("/home/cameron/PycharmProjects/quail")
    subprocess.Popen(['python3', name])

def clicked():
    run_program("animations/bloody yin yang.py")

def click2():
    run_program("animations/solar system.py")

def click3():
    run_program("animations/dvd.py")

row_0 = 0
column_0 = 0
lbl = Label(root, text = "Bloody Yin-Yang")
lbl.grid(column = 0, row = row_0)
btn = Button(root, text = "Start" ,
             fg = "red", command=clicked)
btn.grid(column= 1, row=row_0)

lbl = Label(root, text = "Space")
lbl.grid(column = 0, row = row_0 + 1)
btn = Button(root, text = "Start" ,
             fg = "red", command=click2)
btn.grid(column= 1, row=row_0 + 1)

lbl = Label(root, text = "DVD")
lbl.grid(column = column_0, row = row_0 + 2)
btn = Button(root, text = "Start" ,
             fg = "red", command=click3)
btn.grid(column= 1, row=row_0 + 2)

text_box = Text(root, width=25, height=8, wrap = WORD)
text_box.grid(row=5, column=0, columnspan = 2)

btn = Button(root, text = "Quit", fg = "black", command=root.quit)
btn.grid(column= 99, row=99)

from scripts.python.TTS.pytext import say

def submit_text():
    os.chdir("/home/cameron/PycharmProjects/quail/scripts/python/TTS")
    input_text = text_box.get("1.0", END)  # Get text from textbox
    say(input_text)

def text_clear():
    text_box.delete('1.0', END)

submit_button = Button(root, text="Text-to-Speech", height = 2, command=submit_text)
submit_button.grid(column= 2, row= 5)

clear_button = Button(root, text="CLEAR", fg = "red", command=text_clear)
clear_button.grid(column = 3, row = 5)

# Execute Tkinter
root.mainloop()