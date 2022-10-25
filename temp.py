from time import sleep

from dictionary import create_board
from schiff import (
    SPIELFELDGRÖSSE,
    Coordinate,
    playing_board_pc,
    playing_board_player,
)
from shoot import pc_shoot, player_shoot


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
