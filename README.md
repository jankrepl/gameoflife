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

2. Add pwd to `PYTHONPATH`
```sh
export PYTHONPATH="${PWD}:${PYTHONPATH}"
```

3. Create virtual environment and install dependencies
```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

4. Run via CLI
```sh
./gameoflife/cli.py
```

# TODO
- [ ] Dialog window giving user the chance to select initialization method
- [x] Flake8
- [ ] List all CLI options in README
- [ ] Somehow store interesting initial configurations
- [ ] Add nice gif
- [x] Set up travis
- [ ] Write some tests
- [ ] Include generation number in a small window somewhere
- [ ] Include Pause button
- [ ] Include Restart button
- [ ] Turn into a package and create a CLI entry point

# References
* [Conway's Game of Life (wiki)](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)
* [Python implementation using matplotlib animations](https://github.com/scienceetonnante/GameOfLife)
