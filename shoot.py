"""shoot.py"""

import random

from dictionary import board, create_board, place_ship
from schiff import Schiff


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


def set_ships(one_long: int, two_long: int, three_long: int, four_long: int):
    playing_board = create_board()
    start_point = get_random_field()
    get_direction = random.choice(start_point)
    # vertical
    if get_direction == start_point[0]:
        print("TEst")

    # horizontal
    elif get_direction == start_point[1]:
        for __ in range(one_long):
            end_point = get_direction()
            place_ship(Schiff(start_point, end_point), playing_board)
        for __ in range(one_long):
            end_point = get_direction() + 2
            place_ship(Schiff(start_point, end_point), playing_board)
        for __ in range(one_long):
            end_point = get_direction() + 3
            place_ship(Schiff(start_point, end_point), playing_board)
        for __ in range(one_long):
            end_point = get_direction() + 4
            place_ship(Schiff(start_point, end_point), playing_board)


    print(start_point, get_direction)


set_ships(1, 2, 3, 4)
