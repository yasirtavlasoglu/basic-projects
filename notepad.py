from tkinter import *
from tkinter import filedialog
import tkinter as tk

pad = tk.Tk()
pad.title("Notepad | yasirtavlasoglu")

def cikis():
    global pad
    pad.cikis()

def note():
    global textarea
    return textarea.get("1.0",END)

def kayit():
    global pad
    veri = note()
    dosya = filedialog.asksaveasfile(mode="w",defaultextension=".txt",filetypes=(("Text File",".txt"),("All Files","*.*")),title="Kaydet",initialdir=pad.winfo_pathname)

    if dosya != None:
        dosya.write(veri)
        dosya.close()

def ac():
    global textarea
    dosya = filedialog.askopenfile(mode="r",defaultextension=".txt",filetypes=(("Text File",".txt"),("All Files","*.*")),title="Aç",initialdir=pad.winfo_pathname)

    if dosya == None:
        return
    yazi = dosya.read()
    if yazi != None:
        textarea.delete(1.0,END)
        textarea.insert(END,yazi)

def yeni():
    global textarea
    textarea.delete(1.0,END)

menu = Menu(pad)
dosyamenu = Menu(menu, tearoff=0)
dosyamenu.add_command(label="Yeni",command=yeni)
dosyamenu.add_command(label="Aç",command=ac)
dosyamenu.add_command(label="Kaydet",command=kayit)
dosyamenu.add_separator()
dosyamenu.add_cascade(label="Çıkış",command=cikis)
menu.add_cascade(label="Dosya",menu=dosyamenu)

textarea = Text(pad,width=100,height=20)
textarea.pack()

pad.configure(background="white")
pad.config(menu=menu)
pad.mainloop()
