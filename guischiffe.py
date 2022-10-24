import tkinter as tk
from tkinter import *


class Main( Frame ):
    def __init__( self ):
        tk.Frame.__init__(self)
        self.geometry = Tk(className="Schiffe versenken").geometry("700x700")
        self.master.title("Schiffe versenken")
        self.closebutton = Button(self, text="close", width = 25, command = self.close_window)
        self.closebutton.grid(row = 1, column = 1, columnspan = 2)
    def close_window(self):
        self.destroy()
def main():
    window= Main()
    #window.geometry("700x700")
    window.mainloop()
if __name__ == '__main__':
    main()
