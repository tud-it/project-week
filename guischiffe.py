# import tkinter as tk
# from tkinter import *
# from tkinter import ttk

# board = [['--' for x in range(8)] for x in range(8)]
# def main():
#     window= tk.Tk(className="Schiffe versenken")
#     window.geometry("700x700")
#     window.resizable(False,False)
#     placebutton = ttk.Button(window,text="Schiffe Platzieren",command = "")
#     placebutton.pack(ipadx=2, ipady=5)
#     field = ttk.Frame(window, command=board)
#     field.grid_anchor("w")
#     field.pack()
#     window.mainloop()
# if __name__ == '__main__':
#     main()
import tkinter as tk


class GameBoard(tk.Frame):
    def __init__(self, parent, rows=10, columns=10, size=30, color1="white", color2="lightblue"):
        '''size is the size of a square, in pixels'''

        self.rows = rows
        self.columns = columns
        self.size = size
        self.color1 = color1
        self.color2 = color2
        self.pieces = {}

        canvas_width = columns * size
        canvas_height = rows * size

        tk.Frame.__init__(self, parent)
        self.label = tk.Label(self,text="0")
        self.label.pack(side="right")
        self.button = tk.Button(self,text="shot", command=shuss)
        self.button.pack(side="right")
        self.canvas = tk.Canvas(self, borderwidth=0, highlightthickness=0,
                                width=canvas_width, height=canvas_height, background="bisque")
        self.canvas.pack(side="top", fill=tk.BOTH , expand=True, padx=2, pady=2)

        # this binding will cause a refresh if the user interactively
        # changes the window size
        self.canvas.bind("<Configure>", self.refresh)

    def refresh(self, event):
        '''Redraw the board, possibly in response to window being resized'''
        xsize = int((event.width-1) / self.columns)
        ysize = int((event.height-1) / self.rows)
        self.size = min(xsize, ysize)
        self.canvas.delete("square")
        color = self.color2
        for row in range(self.rows):
            color = self.color1 if color == self.color2 else self.color2
            for col in range(self.columns):
                x1 = (col * self.size)
                y1 = (row * self.size)
                x2 = x1 + self.size
                y2 = y1 + self.size
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill=color, tags="square")
                color = self.color1 if color == self.color2 else self.color2
        for name in self.pieces:
            self.placepiece(name, self.pieces[name][0], self.pieces[name][1])
        self.canvas.tag_raise("piece")
        self.canvas.tag_lower("square")


# image comes from the silk icon set which is under a Creative Commons
# license. For more information see http://www.famfamfam.com/lab/icons/silk/

def shuss():
    board.counter+=1
    board.label['text'] = 'Counter: ' + str(board.counter)

if __name__ == "__main__":
    root = tk.Tk()
    board = GameBoard(root)
    board.counter=0
    board.pack(side="top", fill="both", expand="true", padx=4, pady=4)
    root.mainloop()
