"""main.py"""

import random
from operator import le

from globes import (
    PLAYINGBOARDSIZE,
    Coordinate,
    Schiff,  # player_board,
    create_board,
    num_to_letter,
    pc_board,
    pc_hit,
    pc_miss,
    player_hit,
    player_miss,
    tabulate
)


def place_ship(new_ship: Schiff, board: dict):
    """places ship"""

    # set's horizontal ship
    # FIXME: AttributeError: 'tuple' object has no attribute 'HOR'
    print(new_ship.first, new_ship.last)
    if new_ship.first.HOR == new_ship.last.HOR:
        line = new_ship.first.HOR
        stard: int = new_ship.first.VERT
        end: int = new_ship.last.VERT
        stard=int(stard)
        end=int(end)
        leng = end - stard
        cut = 1

        # test's wether a ship crosses an other
        for i in range(leng):
            if test_space((line, stard + i), board):
                continue
            else:
                cut = 0

        # ship get's set in dictionary
        if cut:
            for i in range(leng):
                board[(line, stard + i)] = True
            return board

        return False

    # set's vertical ship
    # FIXME: AttributeError: 'tuple' object has no attribute 'VERT'
    if new_ship.first.VERT == new_ship.last.VERT:
        spalte = new_ship.first.VERT
        stard = letter_to_num(new_ship.first.HOR)
        end = letter_to_num(new_ship.last.HOR)
        leng = end - stard
        cut = 1

        # test's wether a ship crosses an other
        for i in range(leng):
            if test_space((num_to_letter(stard + i), spalte), board):
                continue
            cut = 0
        # ship get's set in dictionary
        if cut:
            for i in range(leng):
                board[(num_to_letter(stard + i), spalte)] = True
            return board
        return False


def test_space(cell, board: dict):
    """tests key in dic and true"""
    return cell in board and not board.get(cell)


def letter_to_num(letters: str):
    """converts letter strings to numbers"""
    i = 0
    numb = 0
    letters=str(letters)
    for letter in reversed(letters):
        numb += (ord(letter) - 64) * 26**i
        i += 1
    return numb - 1


def ignore_num(zkette: str):
    """ignores input numbers"""
    newstring = ""
    abc = set()
    zkette.upper()
    for i in range(26):
        abc.add(chr(65 + i))
    for character in zkette:
        if character in abc:
            newstring += character
    return newstring


def ignore_float(numb: float):
    """useless_amogus"""
    return int(numb)


def get_random_field():
    board = create_board(PLAYINGBOARDSIZE)
    field_list = list(board.keys())
    field = random.choice(field_list)
    return field


def pc_shoot(count: int):
    """function to shoot a boat"""
    # empty list to store already shot field
    already_shot: list = []
    field = get_random_field()

    if field in already_shot:
        pc_shoot(count)
    # check if ship is on field and shoot it
    if player_board.get(field):
        hit = player_board[field] = False
        count += 1
        pc_hit.append(field)
        return hit, count
    pc_miss.append(field)
    return print("Nicht Getroffen!")


def player_shoot(
    field: Coordinate,
    dic: dict,
):  # count: int):
    """lhfslhk"""
    # check if ship is on field and shoot it
    if dic.get(field):
        hit = dic[field] = False
        # count += 1
        player_hit.append(field)
        return (hit,)  # count
    player_miss.append(field)
    return print("Nicht Getroffen!")


def set_ships_pc(frequency: int, lenght: int):
    """ships"""
    while frequency != 0:
        start_point = get_random_field()
        print(start_point.HOR,start_point.VERT)
        get_direction = random.choice([start_point.HOR, start_point.VERT])

        # vertical
        if get_direction == start_point.HOR:
            if lenght == 1:
                end_point = get_direction
                last_block = Coordinate(get_direction, start_point.VERT)
                kuhl=place_ship(Schiff(start_point, last_block), pc_board)
            else:
                end_point = letter_to_num(get_direction) + lenght
                end_point = num_to_letter(end_point)
                if end_point < PLAYINGBOARDSIZE:
                    last_block = Coordinate(end_point, start_point.VERT)
                    kuhl=place_ship(Schiff(start_point, end_point), pc_board)

        # horizontal
        elif get_direction == start_point.VERT:
            if lenght == 1:
                end_point = get_direction
                last_block = Coordinate(get_direction, start_point.VERT)
                kuhl=place_ship(Schiff(start_point, last_block), pc_board)
            else:
                end_point = get_direction + lenght
                if end_point < PLAYINGBOARDSIZE:
                    last_block = Coordinate(get_direction, start_point.VERT)
                    kuhl=place_ship(Schiff(start_point, last_block), pc_board)
        if not kuhl:
            frequency += 1
        frequency -= 1


def player_move(target: Coordinate):  # , count: int):
    player_shoot(target, pc_board)  # , count)
    return True


# def pc_move(count: int):
#     temp_board = create_board(PLAYINGBOARDSIZE)
#     while player_board != temp_board:
#         pc_shoot(player_board, count)
#         # wait for player move
#         while not player_move():
#             sleep(1)


def test():
    print("es klappt")


# def set_ships_player(ship: Schiff):
#    while frequency != 0:
#        start_point = input()
#        get_direction = input()
#
#        # vertical
#        if get_direction == start_point[0]:
#            if lenght == 1:
#                end_point = get_direction
#                place_ship(Schiff(start_point, end_point), playing_board_pc)
#            else:
#                end_point = letter_to_num(get_direction) + lenght
#                if end_point < SPIELFELDGRÖSSE:
#                    place_ship(Schiff(start_point, end_point), playing_board_pc)
#                    frequency -= 1
#
#        # horizontal
#        elif get_direction == start_point[1]:
#            if lenght == 1:
#                end_point = get_direction
#                place_ship(Schiff(start_point, end_point), playing_board_pc)
#            else:
#                end_point = get_direction + lenght
#                if end_point < SPIELFELDGRÖSSE:
#                    place_ship(Schiff(start_point, end_point), playing_board_pc)
#                    frequency -= 1

set_ships_pc(1,1)
