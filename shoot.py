"""shoot.py"""

import random
from time import sleep

from dictionary import board, create_board, place_ship
from schiff import Schiff, SPIELFELDGRÖSSE


def get_random_field():
    field_list = list(board.keys())
    field = random.choice(field_list)
    return field


def schuss(dic: dict, count: int):
    """function to shoot a boat"""
    # empty list to store already shot field
    already_shot: list = []
    field = get_random_field()

    if field in already_shot:
        schuss(dic, count)
    if dic.get(field):
        hit = dic[field] = False
        count += 1
        return hit, count
    return print("Nicht Getroffen!")


def set_ships(frequency: int, lenght: int):
    playing_board = create_board(SPIELFELDGRÖSSE)
    while frequency != 0:
        start_point = get_random_field()
        get_direction = random.choice(start_point)

        # vertical
        if get_direction == start_point[0]:
            print("TEst")

        # horizontal
        elif get_direction == start_point[1]:
            if lenght == 1:
                end_point = get_direction()
            else:
                end_point = get_direction + lenght
            place_ship(Schiff(start_point, end_point), playing_board)

    return playing_board

def player_move(schiff: Schiff):
    # wait for player move
        while not player_move():
            sleep(1)

def pc_move(schiff: Schiff):
