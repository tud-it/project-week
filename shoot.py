"""shoot.py"""
import random


def schuss(dic, count: int):
    """function to shoot a boat"""
    schiff_b = random.choice("A","B", "C", "D", "F", "G", "H", "I", "J")
    schiff_z = random.int(0, 9)
    schiff = tuple(schiff_b, schiff_z)
    if dic.key(schiff):
        hit = dic.key(schiff) = False
        count += 1
        return hit, count
    else:
        ...
