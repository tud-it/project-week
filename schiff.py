class Coordinate:
    def __init__(self, H: str, V: int):
        self.HOR: str = H
        self.VERT: int = V


class Schiff:
    def __init__(self, f: Coordinate, l: Coordinate):
        self.first: Coordinate = f
        self.last: Coordinate = l


# GLOBAL VALUES
SPIELFELDGRÖSSE = 10
pc_hit: list = []
pc_miss: list = []
player_hit: list = []
player_miss: list = []
