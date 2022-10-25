"""shoot.py"""

import random
from time import sleep

from dictionary import brett, create_board, place_ship
from schiff import Schiff


def get_random_field():
    field_list = list(brett.keys())
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
    playing_board = create_board(10)
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

#         # wait for player move
#         while not player_move():
#             sleep(1)
#     # beende wenn letztes 4er schiff gesunken ist
#     if frequency == 0 and lenght == 4:
#         print("Game over!")

# #def player_move(schiff: Schiff):
