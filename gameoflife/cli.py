#!/usr/bin/env python3

import argparse

from gameoflife.base import Game

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument('--width', type=int, default=75, help='Number of cell columns')
parser.add_argument('--height', type=int, default=50, help='Number of cell rows')
parser.add_argument('--perc', type=int, default=33, help='Percentage of cells that are alive at initialization')

args = parser.parse_args()

# Instantiate the game
game = Game(width=args.width,
            height=args.height)

# Print the representation
print(repr(game))

# Play
game.play(perc=args.perc)
