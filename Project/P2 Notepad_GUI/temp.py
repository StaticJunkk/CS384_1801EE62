import tkinter
from tkinter import *
from tkinter import filedialog
import os
import datetime
from datetime import *




root = Tk()
root.title("Untitled file")
root.geometry('400x400')

def x():
    return

menubar = Menu(root)
filemenu = Menu(menubar)

filemenu.add_command(label='New', command=x, accelerator = 'Ctrl+N')
menubar.add_cascade(label='File', menu=filemenu)



text = Text(root)
text.grid(row = 2)
root.config(menu=menubar)
toolbar = Frame(root)
toolbar.place(relx = 0, rely = 0, anchor = NW)
b1 = Button(toolbar, text = 'Yayya', command = x).pack()


root.mainloop()
