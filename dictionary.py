"""generate playing board"""
from schiff import Schiffe


def create_board():
    """generate playing board"""
    brd = {}
    for i, j in range(10):
        for j in range(10):
            brd[(chr(i + 65), j)] = False
    return brd


board = create_board()


def place_ship(new_ship: Schiffe):
    """plaziert Schiff"""
    if new_ship.first[0] == new_ship.last[0]:
        for i in range(new_ship.last[1] - new_ship.first[1]):
            if new_ship.first in board and not board.get(new_ship.first):
                board[new_ship.first] = True


def test_space(zelle: tuple):
    if zelle in board and not board(zelle):
        return
