import pygame as pg
from dataclasses import dataclass
from math import cos, sin
import random

resolution = 800
columns = 10
dist = resolution // columns
radius = (dist - 20) // 2


@dataclass
class Rotor:
    x: int
    y: int
    speed: float
    horizontal: bool
    angle: float = 0.0
    dot_x: int = 0
    dot_y: int = 0

    def show(self, screen):
        pg.draw.circle(screen, (200, 200, 200), (self.x, self.y), radius, 3)
        pg.draw.circle(screen, (255, 255, 255), (self.dot_x, self.dot_y), 3)

        if self.horizontal:
            pg.draw.line(
                screen, (75, 75, 75), (self.dot_x, self.dot_y), (self.dot_x, resolution)
            )
        else:
            pg.draw.line(
                screen, (75, 75, 75), (self.dot_x, self.dot_y), (resolution, self.dot_y)
            )

    def update(self):
        self.angle += self.speed
        self.dot_x = int(self.x + radius * cos(self.angle))
        self.dot_y = int(self.y + radius * sin(self.angle))


@dataclass
class Lissajous:
    verticies: list

    def update(self, pos):
        self.verticies.append(pos)

    def show(self, screen):
        pg.draw.circle(screen, (255, 255, 255), self.verticies[-1], 2)
        if len(self.verticies) > 1:
            r = random.randint(75, 255)
            g = random.randint(75, 255)
            b = random.randint(75, 255)
            pg.draw.lines(screen, (r, g, b), False, self.verticies, 1)


matrix = [[0] * columns for _ in range(columns)]


def setup():

    for n in range(columns):
        x = dist * n + dist // 2
        y = dist // 2
        # horizontal circles
        matrix[0][n] = Rotor(x, y, 0.01 * n, True)
        # vertical circles
        matrix[n][0] = Rotor(y, x, 0.01 * n, False)

    for row in range(1, columns):
        for column in range(1, columns):
            matrix[row][column] = Lissajous([])


def draw(screen):
    for n in range(1, columns):
        matrix[0][n].update()
        matrix[n][0].update()
        # matrix[0][n].show(screen)
        # matrix[n][0].show(screen)

    for row in range(1, columns):
        for column in range(1, columns):
            x = matrix[0][column].dot_x
            y = matrix[row][0].dot_y
            matrix[row][column].update([x, y])

    for row in range(columns):
        for column in range(columns):

            # get rid of that circle at (0, 0)
            if row == 0 and column == 0:
                continue

            matrix[row][column].show(screen)


def game_loop():

    pg.init()
    screen = pg.display.set_mode([resolution, resolution])

    setup()
    go_on = True
    clock = pg.time.Clock()
    while go_on:
        clock.tick(20)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                go_on = False
        screen.fill((0, 0, 0))
        draw(screen)
        pg.display.flip()

    pg.quit()


def main():
    game_loop()


if __name__ == "__main__":
    main()
