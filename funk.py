
from dictionary import create_board
from schiff import SPIELFELDGRÖSSE


def print_all_fields():
    """print all the fields"""
    brd = create_board(SPIELFELDGRÖSSE)
    feld = list(brd.keys())
    donelist: list = []
    for elem in feld:
        num_string = str(elem[1])
        final_string = elem[0]+num_string
        donelist.append(final_string)
        print(final_string)
#print_all_fields()
