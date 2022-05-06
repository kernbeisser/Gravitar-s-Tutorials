from dataclasses import dataclass
from pickle import TRUE
import random
import pygame as pg


resolution = 512
grid = 20
dist = resolution // grid

mines = 60

matrix = list()

pg.init()
screen = pg.display.set_mode([resolution, resolution])
screen.fill((0, 0, 0))

cell_normal = pg.transform.scale(
    pg.image.load("./data/Teil_10_ms_cell_normal.gif"), (dist, dist)
)
cell_mine = pg.transform.scale(
    pg.image.load("./data/Teil_10_ms_cell_mine.gif"), (dist, dist)
)
cell_marked = pg.transform.scale(
    pg.image.load("./data/Teil_10_ms_cell_marked.gif"), (dist, dist)
)


cell_selected = list()
for n in range(9):
    cell_selected.append(
        pg.transform.scale(
            pg.image.load(f"./data/Teil_10_ms_cell_{n}.gif"), (dist, dist)
        )
    )

neighbour_cells = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


@dataclass
class Cell:
    column: int
    row: int
    mine: bool = False
    selected: bool = False
    flagged: bool = False
    mines_around: int = 0

    def show(self):
        pos = (self.column * dist, self.row * dist)
        if self.selected:
            if self.mine:
                screen.blit(cell_mine, pos)
            else:
                screen.blit(cell_selected[self.mines_around], pos)
        else:
            if self.flagged:
                screen.blit(cell_marked, pos)
            else:
                screen.blit(cell_normal, pos)

    def no_of_mines(self):
        for position in neighbour_cells:
            new_row = self.row + position[0]
            new_column = self.column + position[1]
            if (
                new_row >= 0
                and new_row < grid
                and new_column >= 0
                and new_column < grid
            ):
                if matrix[new_row * grid + new_column].mine:
                    self.mines_around += 1


for n in range(grid * grid):
    matrix.append(Cell(n // grid, n % grid))


while mines > 0:
    mine_pos = random.randrange(grid * grid)
    if not matrix[mine_pos].mine:
        matrix[mine_pos].mine = True
        mines -= 1


for cell in matrix:
    cell.no_of_mines()

def flood_fill(row, column):
    for position in neighbour_cells:
        new_row = row + position[0]
        new_column = column + position[1]
        if (
                new_row >= 0
                and new_row < grid
                and new_column >= 0
                and new_column < grid
            ):
            cell = matrix[new_row*grid + new_column]
            if cell.mines_around == 0 and not cell.selected:
                cell.selected = True
                flood_fill(new_row, new_column)
            else:
                cell.selected = True


def draw():
    for cell in matrix:
        # cell.selected = True
        cell.show()


def game_loop():

    # setup()
    go_on = True
    clock = pg.time.Clock()
    while go_on:
        clock.tick(20)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                go_on = False
            if event.type == pg.MOUSEBUTTONDOWN:
                mounse_x, mounse_y = pg.mouse.get_pos()
                row = mounse_x // dist
                column = mounse_y // dist
                idx = row*grid+column
                cell = matrix[idx]
                if pg.mouse.get_pressed()[2]:
                    cell.flagged = not cell.flagged
                if pg.mouse.get_pressed()[0]:
                    cell.selected = True
                    if cell.mines_around == 0 and not cell.mine:
                        flood_fill(row, column)
                    if cell.mine:
                        for all_cells in matrix:
                            all_cells.selected = True


        draw()
        pg.display.flip()

    pg.quit()


def main():
    game_loop()


if __name__ == "__main__":
    main()
