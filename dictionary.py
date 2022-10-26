"""generate playing board"""
from schiff import Schiff, num_to_letter





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
        start = letter_to_num(new_ship.first.HOR)
        end = letter_to_num(new_ship.last.HOR)
        leng = end - start
        schnitt = 1
        # Test ob neues Schiff ein anderes schneidet
        for i in range(leng):
            if test_space((num_to_letter(start + i), spalte), board):
                continue
            schnitt = 0
        # Schiff wird im Dictionary gesetzt
        if schnitt:
            for i in range(leng):
                board[(num_to_letter(start + i), spalte)] = True
            return board
        return False


def test_space(zelle, board: dict):
    """tests key in dic and true"""
    return zelle in board and not board.get(zelle)





def letter_to_num(buchstaben: str):
    """converts letter strings to numbers"""
    i = 0
    zahl = 0
    for buchstabe in reversed(buchstaben):
        zahl += (ord(buchstabe) - 64) * 26**i
        i += 1
    return zahl - 1


def ignore_num(zkette: str):
    """ignores input numbers"""
    neukette = ""
    abc = set()
    zkette.upper()
    for i in range(26):
        abc.add(chr(65 + i))
    for zeichen in zkette:
        if zeichen in abc:
            neukette += zeichen
    return neukette


def ignore_float(zahl: float):
    """useless"""
    return int(zahl)


# print(letter_to_num("ABC"))
# print(num_to_letter(500))
