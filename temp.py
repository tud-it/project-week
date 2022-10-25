from schiff import Coordinate
from shoot import player_shoot


def player_move(
    target: Coordinate,
):
    player_shoot(
        target,
    )
    return True


def pc_move():
    # wait for player move
    while not player_move():
        sleep(1)
