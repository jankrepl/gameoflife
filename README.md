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

2. Create virtual environment and install dependencies
```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Run via CLI
```sh
./gameoflife/cli.py
```

# TODO
- [ ] Dialog window giving user the chance to select initialization method
- [ ] Flake8
- [ ] Somehow store interesting initial configurations
- [ ] Add nice gif


# References
* [Conway's Game of Life (wiki)](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)
* [Python implementation using matplotlib animations](https://github.com/scienceetonnante/GameOfLife)
