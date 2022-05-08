# imports as needed
import pygame as pg
from math import pi, sin, cos
# import random


class ClassName:
    def __init__(self):
        self.width = 1024
        self.height = 1024
        self.screen = None
        self.clock = None
        self.centre = (self.width // 2, self.height // 2)
        self.centre_x, self.centre_y = self.centre
        self.radius = self.width // 2 - 16
        self.screen = None


    def setup(self):
        pg.init()
        self.screen = pg.display.set_mode((self.width, self.height))
        self.clock = pg.time.Clock()

    def draw(self):
        pg.draw.circle(self.screen, (255, 255, 255), self.centre, self.radius, 2)

    def game_loop(self):

        self.setup()
        self.draw()
        
        go_on = True
        while go_on:
            self.clock.tick(60)
            for event in pg.event.get():
                if event.type == pg.QUIT or (
                    event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE
                ):
                    go_on = False

            pg.display.flip()

        pg.quit()


def main():
    cn = ClassName()
    cn.game_loop()


if __name__ == "__main__":
    main()
