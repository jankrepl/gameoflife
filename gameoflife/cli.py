#!/usr/bin/env python3

import argparse

from gameoflife.base import Game

parser = argparse.ArgumentParser()

parser.add_argument('--width', type=int, default=50)
parser.add_argument('--height', type=int, default=50)

args = parser.parse_args()

# Instantiate the game
game = Game(width=args.width,
            height=args.height)

# Print the representation
print(repr(game))

# Play
game.play()
