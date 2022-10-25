"""generate playing board"""
from schiff import Schiff


def create_board():
    """generate playing board"""
    brd = {}
    for i in range(10):
        for j in range(10):
            brd[(chr(i + 65), j)] = False
    return brd


brett = create_board()


def place_ship(new_ship: Schiff, board: dict):
    """plaziert Schiff"""

    if new_ship.first.HOR == new_ship.last.HOR:
        zeile = new_ship.first.HOR
        start = new_ship.first.VERT
        end = new_ship.last.VERT
        leng = end - start
        schnitt = 1
        for i in range(leng):
            if test_space((zeile, start + i), board):
                continue
            schnitt = 0
        if schnitt:
            for i in range(leng):
                board[(zeile, start + i)] = True
            return board
        return False

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
