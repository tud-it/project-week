class Coordinate:
    def __init__(self, H: str, V: int):
        self.HOR: str = H
        self.VERT: int = V


class Schiff:
    def __init__(self, f: Coordinate, l: Coordinate):
        self.first: Coordinate = f
        self.last: Coordinate = l
