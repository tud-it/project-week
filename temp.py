def player_move(schiff: Schiff):
    # wait for player move
        while not player_move():
            sleep(1)

def pc_move(schiff: Schiff):
