import pygame as pg
from dataclasses import dataclass

resolution = 1024
columns = 5
dist = resolution // columns
radius = (dist - 20) // 2

matrix = [[0] * columns for _ in range(columns)]

for n in range(columns):
    x = dist * n + dist // 2
    y = dist // 2


@dataclass
class Rotor:
    x : int
    y : int
    speed : float
    horizontal : bool
    angle : float = 0.0


def game_loop():

    pg.init()
    screen = pg.display.set_mode([resolution, resolution])

    go_on = True
    while go_on:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                go_on = False
        screen.fill((0, 0, 0))
        for n in range(columns):
            pg.draw.circle(screen, (0, 255, 0),
                           (dist * n + dist//2, dist//2), radius, 3)
            pg.draw.circle(screen, (0, 255, 0),
                           (dist//2, dist * n + dist//2), radius, 3)
        pg.display.flip()

    pg.quit()


def main():
    game_loop()


if __name__ == '__main__':
    main()
