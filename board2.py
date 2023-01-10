"""playing board 2"""

from tabulate import tabulate

from globes import (
    PLAYINGBOARDSIZE,
    create_board,
    num_to_letter,
    player_hit,
    player_miss,
)

spalten: list = []
zeilen: list = []
hit_miss = create_board(PLAYINGBOARDSIZE)
for element in player_hit:
    hit_miss[element] = "hit"
for element in player_miss:
    hit_miss[element] = "miss"
for j in range(PLAYINGBOARDSIZE + 1):
    spalten.clear()
    for i in range(PLAYINGBOARDSIZE + 2):
        if hit_miss.get((num_to_letter(j), i)) == "hit":
            spalten.append("❌")
        elif hit_miss.get((num_to_letter(j), i)) == "miss":
            spalten.append("⭕️")
        else:
            spalten.append(" ")
    zeilen.append(spalten[0:-1])


def table(tabelle):
    print(tabulate(tabelle, tablefmt="html"))


table(zeilen)
