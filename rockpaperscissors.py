#!/usr/dev/env python3.9
import random

def game():
    mh_choice = random.choice(("r", "p", "s"))
    us_choice = input("coose rock (c), paper (p), or scissots (s): ")
    if us_choice == mh_choice:
        return "It's a tie!"
    if is_win(us_choice, mh_choice):
        return "You Won!!"
    return 'You lost'

    # r > s, s > p, p > r
def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

print(game())

