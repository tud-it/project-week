"""generate playing board"""
from schiff import Schiff


def create_board():
    """generate playing board"""
    brd = {}
    for i in range(10):
        for j in range(10):
            brd[(chr(i + 65), j)] = False
    return brd


board = create_board()


def place_ship(new_ship: Schiff):
    """plaziert Schiff"""
    if new_ship.first.HOR == new_ship.last.HOR:
        zeile = new_ship.first.HOR
        start = new_ship.first.VERT
        end = new_ship.last.VERT
        leng = end - start
        for i in range(leng):
            test_space((zeile, start + i))
        for i in range(leng):
            change_board((zeile, start + i))

    elif new_ship.first.VERT == new_ship.last.VERT:
        spalte = new_ship.first.VERT
        start = ord(new_ship.first.HOR)
        end = ord(new_ship.last.HOR)
        leng = end - start
        for i in range(leng):
            test_space((chr(start + i), spalte))
        for i in range(leng):
            change_board((chr(start + i), spalte))


def change_board(zelle):
    board[zelle] = True


def test_space(zelle):
    return zelle in board and not board.get(zelle)
