import numpy as np
import pygame

pygame.init()

BACKGROUND_COLOR = (0, 0, 0)
ALIVE_COLOR = (0, 255, 0)
DEAD_COLOR = (255, 0, 0)

FONT_TYPE = 'Arial'


class BackEnd:
    """Grid representation of the living and dead cells.

    Notes
    -----
    Total number of cells is width * height

    Parameters
    ----------
    height : int
        Number of rows in the cell grid.

    widght : int
        Number of columns in the cell grid.

    Attributes
    ----------
    grid : ndarray
        2-d arrays of dtype=bool. If a given element is True, then it represents a living cell.
    """

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

        self.grid[:] = False
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
    def __init__(self, width, height, gap=1, cell_size=12, vertical_margin=80):

        self.width = width
        self.height = height
        self.gap = gap
        self.cell_size = cell_size
        self.vertical_margin = vertical_margin

        self.screen_width = width * (cell_size + gap) - gap
        self.screen_height = height * (cell_size + gap) - gap + vertical_margin

        # Instantiate inner attributes
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.font = pygame.font.SysFont(FONT_TYPE, (vertical_margin // 2))

        self.backend = BackEnd(height=self.height, width=self.width)

    def __repr__(self):
        return f'Game(width={self.width}, height={self.height})'

    def play(self, perc=50):
        """Play the game.

        Parameters
        ----------
        perc : int
            Percentage of all cells that are randomly set to be alive at initialization.
        """

        if not 0 <= perc <= 100:
            raise ValueError('Percentage needs to be between 0 and 100')

        n_overall = self.width * self.height
        n_initial = int(n_overall * (perc / 100))
        initial_ix = np.random.choice(n_overall, size=n_initial, replace=False)

        initial_list_x = initial_ix // self.width
        initial_list_y = initial_ix % self.width

        initial_list = list(zip(initial_list_x, initial_list_y))

        self.backend.initial_configuration(initial_list)

        # Variables
        game_over = False  # game status indicator
        paused = False  # freeze program
        step = False   # used to step 1 iteration forward in the paused mode
        rerun = False  # exit the game and start a new one

        n_gen = 0

        self.screen.fill(BACKGROUND_COLOR)

        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        paused = not paused

                    elif event.key == pygame.K_ESCAPE:
                        game_over = True

                    elif event.key == pygame.K_r:
                        rerun = True
                        game_over = True

                    elif event.key == pygame.K_s:
                        if paused:
                            step = True

            if paused:
                if step:
                    step = False  # disables paused for 1 iteration
                else:
                    continue

            # Draw
            self.draw_grid()
            self.draw_lower_bar()
            self.draw_counter(n_gen)

            # Evolve
            self.backend.evolve()

            # Display
            pygame.display.flip()
            # pygame.display.update()

            n_gen += 1
            print(n_gen)

            # pygame.display.update()

        if rerun:
            self.play()

        pygame.quit()

    def draw_grid(self):
        """Draw cell grid."""

        for r in range(self.height):
            screen_r = r * (self.cell_size + self.gap) - self.gap
            for c in range(self.width):
                screen_c = c * (self.cell_size + self.gap) - self.gap
                color = ALIVE_COLOR if self.backend.grid[r, c] else DEAD_COLOR
                pygame.draw.rect(self.screen, color, [screen_c, screen_r, self.cell_size, self.cell_size])

    def draw_lower_bar(self):
        """Draw status lower bar."""

        start_r = self.screen_height - self.vertical_margin
        pygame.draw.rect(self.screen, (0, 0, 255), [0, start_r, self.screen_width, self.vertical_margin])

    def draw_counter(self, n_gen):
        """Draw generation counter."""

        text = self.font.render(f'Generation {n_gen}!', True, (255, 0, 0))
        text_rect = text.get_rect(center=(self.screen_width / 2, self.screen_height - (self.vertical_margin / 2)))
        self.screen.blit(text, text_rect)
