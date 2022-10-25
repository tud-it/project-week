"""generate playing board"""
from schiff import Schiff


def create_board(groesse):
    """generate playing board"""
    brd = {}
    for i in range(groesse):
        for j in range(groesse):
            brd[(num_to_letter(i), j)] = False
    return brd


# brett = create_board(10)


def place_ship(new_ship: Schiff, board: dict):
    """plaziert Schiff"""
    # setzen horizontales Schiff
    if new_ship.first.HOR == new_ship.last.HOR:
        zeile = new_ship.first.HOR
        start = new_ship.first.VERT
        end = new_ship.last.VERT
        leng = end - start
        schnitt = 1
        # Test ob neues Schiff ein anderes schneidet
        for i in range(leng):
            if test_space((zeile, start + i), board):
                continue
            else:
                schnitt = 0
        # Schiff wird im Dictionary gesetzt
        if schnitt:
            for i in range(leng):
                board[(zeile, start + i)] = True
            return board

        return False
    # setzen vertikales Schiff
    if new_ship.first.VERT == new_ship.last.VERT:
        spalte = new_ship.first.VERT
        start = ord(new_ship.first.HOR)
        end = ord(new_ship.last.HOR)
        leng = end - start
        schnitt = 1
        # Test ob neues Schiff ein anderes schneidet
        for i in range(leng):
            if test_space((chr(start + i), spalte), board):
                continue
            schnitt = 0
        # Schiff wird im Dictionary gesetzt
        if schnitt:
            for i in range(leng):
                board[(chr(start + i), spalte)] = True
            return board
        return False


def test_space(zelle, board: dict):
    return zelle in board and not board.get(zelle)


def num_to_letter(num: int):
    if num < 26:
        buchstabe = chr(num + 65)
        return buchstabe

    buchstabe1 = num_to_letter(int(num / 26))
    num -= 26 * int(num / 26)
    buchstabe2 = num_to_letter(num)
    buchstaben = buchstabe1 + buchstabe2
    return buchstaben


def letter_to_num(buchstaben: str):
    zahl = ord(buchstaben[-1]) - 65
    buchstaben = buchstaben[:-1]
    zahl+=
    return zahl


print(letter_to_num("A"))
# print(num_to_letter(500))
