import tkinter as tk
from cgitb import text

from dictionary import create_board
from schiff import Schiff
from shoot import schuss, set_ships


class GameBoard(tk.Frame):
    def __init__(
        self,
        parent,
        rows=10,
        columns=10,
        size=30,
        color1="white",
        color2="lightblue",
    ):
        """size is the size of a square, in pixels"""

        self.rows = rows
        self.columns = columns
        self.size = size
        self.color1 = color1
        self.color2 = color2
        self.pieces = {}

        canvas_width = columns * size
        canvas_height = rows * size

        tk.Frame.__init__(self, parent)
        #create field and buttons
        self.label = tk.Label(self, text="0")
        self.label.pack(side="right")
        self.label_score = tk.Label(self, text="Treffer:")
        self.label_score.pack(anchor="w")
        self.button_score=tk.Button(self,text="score", command=score)
        self.button_score.pack(anchor="w")
        # self.button_shoot=tk.Button(self,text="shoot",command=schuss(create_board,0))
        # self.button_shoot.pack(anchor="e")
        #create entrys to get numbers of ships to place
        self.length1 = tk.Entry(self, textvariable=text)
        self.label_leng1 = tk.Label(self, text="Length one:")
        self.label_leng1.pack(anchor="n")
        self.length1.pack(anchor="n")
        self.ships_with_lengt_one = self.length1.get()
        self.length2 = tk.Entry(self, textvariable=text)
        self.label_leng2 = tk.Label(self, text="Length two:")
        self.label_leng2.pack(anchor="n")
        self.length2.pack(anchor="n")
        self.ships_with_lengt_two = self.length2.get()
        self.length3 = tk.Entry(self, textvariable=text)
        self.label_leng3 = tk.Label(self, text="Length three:")
        self.label_leng3.pack(anchor="n")
        self.length3.pack(anchor="n")
        self.ships_with_lengt_three = self.length3.get()
        self.length4 = tk.Entry(self, textvariable=text)
        self.label_leng4 = tk.Label(self, text="Length four:")
        self.label_leng4.pack(anchor="n")
        self.length4.pack(anchor="n")
        self.ships_with_lengt_four = self.length4.get()
        # self.button_place=tk.Button(self,text="Place", command=set_ships(Schiff(1,self.ships_with_lengt_one),create_board))
        # self.button_place.pack(anchor="ne")
        #self.button = tk.Button(self, text="shot", command=schuss(place_ship, board.counter))
        #self.button.pack(side="right") #still not useable
        self.button_newgame=tk.Button(self,text="New Game",command=self.reload)
        self.button_newgame.pack(anchor="se")
        self.canvas = tk.Canvas(
            self,
            borderwidth=0,
            highlightthickness=0,
            width=canvas_width,
            height=canvas_height,
            background="bisque",
        )
        self.canvas.pack(side="top", fill=tk.BOTH, expand=True, padx=2, pady=2)

        # this binding will cause a refresh if the user interactively
        # changes the window size
        self.canvas.bind("<Configure>", self.refresh)

    def refresh(self, event):
        """Redraw the board, possibly in response to window being resized"""
        xsize = int((event.width - 1) / self.columns)
        ysize = int((event.height - 1) / self.rows)
        self.size = min(xsize, ysize)
        self.canvas.delete("square")
        color = self.color2
        for row in range(self.rows):
            color = self.color1 if color == self.color2 else self.color2
            for col in range(self.columns):
                x1 = col * self.size
                y1 = row * self.size
                x2 = x1 + self.size
                y2 = y1 + self.size
                self.canvas.create_rectangle(
                    x1, y1, x2, y2, outline="black", fill=color, tags="square"
                )
                color = self.color1 if color == self.color2 else self.color2
        self.canvas.tag_raise("piece")
        self.canvas.tag_lower("square")

    def reload(self):
        self.update()

def shoot():
    board.counter+=1
    label=board.label
    label['text']= board.counter
def score():
    board.score+=1
    board.label_score['text']=f"Treffer: {board.score}"
if __name__ == "__main__":
    root = tk.Tk()
    board = GameBoard(root)
    board.counter = 0 #for counting the shots
    board.score = 0 #for counting the hits
    board.pack(side="top", fill="both", expand="true", padx=4, pady=4)
    root.mainloop()
