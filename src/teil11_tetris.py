# imports as needed
from dataclasses import dataclass
import pygame as pg
import random

WIDTH, COLUMNS, ROWS = 400, 10, 20
DIST = WIDTH // COLUMNS
HEIGHT = DIST * ROWS
GRID = [0] * COLUMNS * ROWS

TRETROMINOEDOWN = pg.USEREVENT + 1
SPEEDUP = pg.USEREVENT + 2

tile_speed = 500

pg.init()
screen = pg.display.set_mode([WIDTH, HEIGHT])

pg.time.set_timer(TRETROMINOEDOWN, tile_speed)
pg.time.set_timer(SPEEDUP, 30_000)
# pg.key.set_repeat(1, 100)

# tetrominoes = [[0 for _ in range(4)] * 4 for _ in range(7)]

tetrominoes = [
    [0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 5, 5, 5, 0, 0, 0, 5, 0, 0, 0, 0, 0],
    [0, 0, 7, 0, 7, 7, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 2, 2, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [4, 4, 0, 0, 0, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 6, 6, 6, 0, 0, 6, 0, 0, 0, 0, 0, 0],
]

# GRID[0] = 3
# GRID[1] = 3

tiles = list()
for n in range(8):
    tiles.append(
        pg.transform.scale(pg.image.load(f"./data/Teil_11_tt3_{n}.gif"), (DIST, DIST))
    )


@dataclass
class Tetrominoe:
    tet: list
    row: int = 0
    column: int = 3

    def show(self):
        for n, color in enumerate(self.tet):
            if color > 0:
                column = (self.row + n // 4) * DIST
                row = (self.column + n % 4) * DIST
                screen.blit(tiles[color], (row, column))

    def valid_position(self, r, c):
        for n, color in enumerate(self.tet):
            if color > 0:
                row = r + n // 4
                column = c + n % 4
                if (
                    row >= ROWS
                    or column < 0
                    or column >= COLUMNS
                    or GRID[row * COLUMNS + column] > 0
                ):
                    return False
        return True

    def update(self, row_offset, column_offset):
        if self.valid_position(self.row + row_offset, self.column + column_offset):
            self.row += row_offset
            self.column += column_offset
            return True
        return False

    def rotate(self):
        # print("da dreht sich mal gar nix...")
        save_tetrominoe = self.tet.copy()
        for n, color in enumerate(save_tetrominoe):
            row = n // 4
            column = n % 4
            self.tet[(2 - column) * 4 + row] = color

        if not self.valid_position(self.row, self.column):
            self.tet = save_tetrominoe.copy()


def figure_to_grid():
    for n, color in enumerate(figure.tet):
        if color > 0:
            row = figure.row + n // 4
            column = figure.column + n % 4
            GRID[row * column + column] = color


def remove_completed_line():
    for row in range(ROWS):
        for column in range(COLUMNS):
            if GRID[row * COLUMNS + column] == 0:
                break
            else:
                del GRID[row * COLUMNS : row * COLUMNS + COLUMNS]
                GRID[0:0] = [0] * COLUMNS


clock = pg.time.Clock()
go_on = True
figure = Tetrominoe(tetrominoes[random.randrange(7)])

while go_on:
    clock.tick(20)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            go_on = False

        if event.type == TRETROMINOEDOWN:
            if not figure.update(1, 0):
                figure_to_grid()
                remove_completed_line()
                figure = Tetrominoe(tetrominoes[random.randrange(7)])

        if event.type == SPEEDUP:
            tile_speed = int(tile_speed * 0.8)
            pg.time.set_timer(TRETROMINOEDOWN, tile_speed)

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                figure.update(0, -1)
            if event.key == pg.K_RIGHT:
                figure.update(0, 1)
            if event.key == pg.K_DOWN:
                figure.update(1, 0)
            if event.key == pg.K_LCTRL:
                figure.rotate()

    screen.fill((0, 0, 0))

    for n, color in enumerate(GRID):
        if color > 0:
            x = n % COLUMNS * DIST
            y = n % ROWS * DIST
            screen.blit(tiles[color], (x, y))

    figure.show()
    pg.display.flip()

pg.quit()


def main():
    pass


if __name__ == "__main__":
    main()
