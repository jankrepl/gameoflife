import numpy as np
import pygame

pygame.init()

BACKGROUND_COLOR = (0, 0, 0)
ALIVE_COLOR = (0, 255, 0)
DEAD_COLOR = (255, 0, 0)


class BackEnd:

    def __init__(self, height=400, width=400):

        self.height = height
        self.width = width

        self.grid = np.empty((self.height, self.width), dtype=bool)
        self.grid[:] = False  # not necessary

    def initial_configuration(self, initial_list):
        """Initialize the grid with an initial structure.

        Parameters
        ----------
        initial_list : list[tuple]
            List of tuples each of form (r, c) where r is the row and c is the column.
        """
        xy_tuple = tuple(zip(*initial_list))
        self.grid[xy_tuple] = True

    def evolve(self):
        """Given the current grid state, evolve."""

        grid_num = self.grid.astype(int)

        # Assume that all cells on the boundaries (row/column end) will die
        neighbours_alive = np.zeros((self.height, self.width))

        neighbours_alive[1:-1, 1:-1] = (grid_num[:-2, :-2] + grid_num[:-2, 1:-1] + grid_num[:-2, 2:] +
                                        grid_num[1:-1, :-2] + grid_num[1:-1, 2:] + grid_num[2:, :-2] +
                                        grid_num[2:, 1:-1] + grid_num[2:, 2:])

        self.grid = np.logical_or(np.logical_and(self.grid, np.logical_or(neighbours_alive == 2,
                                                                          neighbours_alive == 3)),
                                  np.logical_and(~self.grid, neighbours_alive == 3))

    def __str__(self):
        return str(self.grid)


class Game:
    def __init__(self, width, height, gap=1, cell_size=15):

        self.width = width
        self.height = height
        self.gap = gap
        self.cell_size = cell_size

        self.screen_width = width * (cell_size + gap) - gap
        self.screen_height = height * (cell_size + gap) - gap

        # Instantiate inner attributes
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.backend = BackEnd(height=self.height, width=self.width)

    def __repr__(self):
        return f'Game(width={self.width}, height={self.height})'

    def play(self, init_method='random'):

        if init_method == 'random':
            # Generate random initial setup
            n_initial = (self.width * self.height) // 3  # cca 1/3 of all cells alive
            initial_list_x = np.random.randint(self.height, size=n_initial)
            initial_list_y = np.random.randint(self.width, size=n_initial)

            initial_list = list(zip(initial_list_x, initial_list_y))

        else:
            raise ValueError('Unknown init_method')

        self.backend.initial_configuration(initial_list)

        done = False
        n_gen = 0
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

            self.screen.fill(BACKGROUND_COLOR)
            self.draw_grid()
            self.backend.evolve()
            pygame.display.flip()

            n_gen += 1
            print(n_gen)

            # pygame.display.update()

    def draw_grid(self):
        for r in range(self.height):
            screen_r = r * (self.cell_size + self.gap) - self.gap
            for c in range(self.width):
                screen_c = c * (self.cell_size + self.gap) - self.gap
                color = ALIVE_COLOR if self.backend.grid[r, c] else DEAD_COLOR
                pygame.draw.rect(self.screen, color, [screen_c, screen_r, self.cell_size, self.cell_size])
