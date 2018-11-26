# Game of Life using PyGame
Minimal python implementation of Game of Life using PyGame for visualization.

# Demo
![](https://github.com/jankrepl/gameoflife/blob/master/images/demo.gif)


# Usage
1. Clone
```sh
git clone https://github.com/jankrepl/gameoflife.git
cd gameoflife
```

2. Create virtual environment
```sh
python3 -m venv venv
source venv/bin/activate
```

3. Install via `setup.py`
```sh
pip install .
```

4. Run via CLI
```sh
gol
```
See below optional arguments
```sh
usage: gol [-h] [--width WIDTH] [--height HEIGHT] [--perc PERC]

optional arguments:
  -h, --help       show this help message and exit
  --width WIDTH    Number of cell columns (default: 75)
  --height HEIGHT  Number of cell rows (default: 50)
  --perc PERC      Percentage of cells that are alive at initialization
                   (default: 33)
```

# Controls

* <kbd>⎋ Escape</kbd> — Exit
* <kbd>r</kbd> — Restart
* <kbd>Space</kbd> — Pause
* <kbd>s</kbd> — Single step (only active in Pause mode)


# TODO
- [ ] Better behavior around the borders (currently weird)

# References
* [Conway's Game of Life (wiki)](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)
* [Python implementation using matplotlib animations](https://github.com/scienceetonnante/GameOfLife)
