from tabulate import tabulate


class Coordinate:
    def __init__(self, H: str, V: int):
        self.HOR: str = H
        self.VERT: int = V


class Schiff:
    def __init__(self, f: Coordinate, l: Coordinate):
        self.first: Coordinate = f
        self.last: Coordinate = l


def create_board(groesse):
    """generate playing board"""
    brd = {}
    for i in range(groesse):
        for j in range(groesse):
            brd[(num_to_letter(i), j)] = False
    return brd


def num_to_letter(num: int):
    """converts numbers into letters and greater numbers to (ABC)"""
    if num < 26:
        buchstabe = chr(num + 65)
        return buchstabe

    buchstabe1 = num_to_letter(int(num / 26) - 1)
    num -= 26 * int(num / 26)
    buchstabe2 = num_to_letter(num)
    buchstaben = buchstabe1 + buchstabe2
    return buchstaben


# GLOBAL VALUES
PLAYINGBOARDSIZE = 10
player_hit: list = []
player_miss: list = []
player_board = create_board(PLAYINGBOARDSIZE)
pc_hit: list = []
pc_miss: list = []
pc_board = create_board(PLAYINGBOARDSIZE)


# from schiff import playing_board_player
def table(tabelle):

    print(tabulate(tabelle, tablefmt="html"))
