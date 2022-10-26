from game import create_board


class Coordinate:
    """Defines Coordinats"""

    def __init__(self, H: str, V: int):
        self.HOR: str = H
        self.VERT: int = V


class Ship:
    """Defines a Ship"""

    def __init__(self, f: Coordinate, l: Coordinate):
        self.first: Coordinate = f
        self.last: Coordinate = l

# GLOBAL VALUES
PLAYINGBOARDSIZE = 10
player1_hit: list = []
player1_miss: list = []
player1_board = create_board(PLAYINGBOARDSIZE)
player2_hit: list = []
player2_miss: list = []
player2_board = create_board(PLAYINGBOARDSIZE)
