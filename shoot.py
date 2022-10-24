"""shoot.py"""

import random

from dictionary import board


def schuss(dic: dict, count: int):
    """function to shoot a boat"""
    field_list = list(board.keys())
    field = random.choice(field_list)

    # empty list to store already shot field
    already_shot: list = []

    if field in already_shot:
        schuss(dic, count)
    if dic.get(field):
        hit = dic[field] = False
        count += 1
        return hit, count
    return print("Nicht Getroffen!")
