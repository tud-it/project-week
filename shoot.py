"""shoot.py"""

import random
from time import sleep

from dictionary import create_board, letter_to_num, place_ship
from schiff import (
    SPIELFELDGRÖSSE,
    Coordinate,
    Schiff,
    pc_hit,
    pc_miss,
    player_hit,
    player_miss,
)


def get_random_field():
    board = create_board(SPIELFELDGRÖSSE)
    field_list = list(board.keys())
    field = random.choice(field_list)
    return field


def pc_shoot(dic: dict, count: int):
    """function to shoot a boat"""
    # empty list to store already shot field
    already_shot: list = []
    field = get_random_field()

    if field in already_shot:
        pc_shoot(dic, count)
    # check if ship is on field and shoot it
    if dic.get(field):
        hit = dic[field] = False
        count += 1
        pc_hit.append(field)
        return hit, count
    pc_miss.append(field)
    return print("Nicht Getroffen!")


def player_shoot(field: Coordinate, dic: dict, count: int):
    """lhfslhk"""
    # check if ship is on field and shoot it
    if dic.get(field):
        hit = dic[field] = False
        count += 1
        player_hit.append(field)
        return hit, count
    player_miss.append(field)
    return print("Nicht Getroffen!")


def set_ships(frequency: int, lenght: int):
    playing_board = create_board(SPIELFELDGRÖSSE)
    while frequency != 0:
        start_point = get_random_field()
        get_direction = random.choice(start_point)

        # vertical
        if get_direction == start_point[0]:
            if lenght == 1:
                end_point = get_direction
            else:
                end_point = letter_to_num(get_direction) + lenght
            place_ship(Schiff(start_point, end_point), playing_board)

        # horizontal
        elif get_direction == start_point[1]:
            if lenght == 1:
                end_point = get_direction
            else:
                end_point = get_direction + lenght
            place_ship(Schiff(start_point, end_point), playing_board)

    return playing_board
