#!/usr/bin/env python3

import argparse

from gameoflife.base import Game

parser = argparse.ArgumentParser()

parser.add_argument('--width', type=int, default=50)
parser.add_argument('--height', type=int, default=50)

args = parser.parse_args()


game = Game(width=args.width,
            height=args.height)




print(repr(game))

game.play()