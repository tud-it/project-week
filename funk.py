
from dictionary import create_board
from schiff import SPIELFELDGRÖSSE


def print_all_fields():
    """print all the fields"""
    brd = create_board(SPIELFELDGRÖSSE)
    feld = list(brd.keys())
    for elem in feld:
        num_string = str(elem[1])
        final_string = elem[0]+num_string
        return final_string
print_all_fields()
