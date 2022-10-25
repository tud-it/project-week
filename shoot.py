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
    playing_board_pc,
    playing_board_player,
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


def set_ships_pc(frequency: int, lenght: int):
    while frequency != 0:
        start_point = get_random_field()
        get_direction = random.choice(start_point)

        # vertical
        if get_direction == start_point[0]:
            if lenght == 1:
                end_point = get_direction
                place_ship(Schiff(start_point, end_point), playing_board_pc)
            else:
                end_point = letter_to_num(get_direction) + lenght
                if end_point < SPIELFELDGRÖSSE:
                    place_ship(Schiff(start_point, end_point), playing_board_pc)
                    frequency -= 1

        # horizontal
        elif get_direction == start_point[1]:
            if lenght == 1:
                end_point = get_direction
                place_ship(Schiff(start_point, end_point), playing_board_pc)
            else:
                end_point = get_direction + lenght
                if end_point < SPIELFELDGRÖSSE:
                    place_ship(Schiff(start_point, end_point), playing_board_pc)
                    frequency -= 1


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


def player_move(target: Coordinate, count: int):
    player_shoot(target, playing_board_pc, count)
    return True


def pc_move(count: int):
    temp_board = create_board(SPIELFELDGRÖSSE)
    while playing_board_player != temp_board:
        pc_shoot(playing_board_player, count)
        # wait for player move
        while not player_move:
            sleep(1)
