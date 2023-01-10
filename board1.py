"""playing board 1"""
# from js import document
from tabulate import tabulate

from globes import PLAYINGBOARDSIZE, num_to_letter, player_board

spalten: list = []
zeilen: list = []
for j in range(PLAYINGBOARDSIZE + 1):
    spalten.clear()
    if j:
        for i in range(PLAYINGBOARDSIZE + 2):
            if i:
                if player_board.get((num_to_letter(j), i)):
                    spalten.append("🛥")
                else:
                    spalten.append(" ")
            else:
                spalten.append(j - 1)
    else:
        for i in range(PLAYINGBOARDSIZE + 2):
            if i:
                spalten.append(num_to_letter(i - 1))
            else:
                spalten.append(" ")
    zeilen.append(spalten[0:-1])


def table(tabelle):
    return tabulate(tabelle, tablefmt="html")


print(table(zeilen))
