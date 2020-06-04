import os
from tkinter import *
from tkinter import messagebox
def st():
    os.system("shutdown /r /t 5")
def nst():
    exit()
box = Tk()
box.geometry('210x80')

lbl = Label(box,text = 'Are you sure want to restart this PC?')
lbl.grid(column  = 1,row = 1)

yes = Button(box,text = 'Yes',command = st)
yes.grid(column = 1,row = 2)

no = Button(box,text = 'No',command = nst)
no.grid(column = 1,row = 3)

