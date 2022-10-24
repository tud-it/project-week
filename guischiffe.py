import tkinter as tk
from tkinter import *
from tkinter import ttk


def main():
    window= tk.Tk(className="Schiffe versenken")
    window.geometry("700x700")
    window.resizable(False,False)
    placebutton = ttk.Button(window,text="Schiffe Platzieren",command = "")
    placebutton.pack(ipadx=2, ipady=5)
    field = ttk.Frame(window, height=20, width=20, borderwidth=1,relief=SOLID)
    field.anchor("center")
    field.pack()
    window.mainloop()
if __name__ == '__main__':
    main()
