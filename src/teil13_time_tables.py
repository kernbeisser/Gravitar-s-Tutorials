# imports as needed
import pygame as pg
from math import pi, sin, cos
import random


class TimeTables:
    def __init__(self):
        self.width = 1024
        self.height = 1024
        self.centre = (self.width // 2, self.height // 2)
        self.centre_x, self.centre_y = self.centre
        self.radius = self.width // 2 - 16
        self.screen = None
        self.screen2 = None
        self.screen3 = None
        self.color = None
        self.clock = None
        self.section = 200
        self.angle = 2 * pi / self.section
        self.points = list()
        self.factor = 0

    def setup(self):
        pg.init()
        self.screen = pg.display.set_mode((self.width, self.height))
        self.screen2 = pg.Surface((self.width, self.height))
        self.clock = pg.time.Clock()
        self.color = pg.Color(150,150,150)

    def draw(self):
        pg.draw.circle(self.screen2, (255, 255, 255), self.centre, self.radius, 2)
        for point in range(self.section):
            x = int(self.radius * cos(self.angle * point) + self.centre_x + pi)
            y = int(self.radius * sin(self.angle * point) + self.centre_y + pi)
            pg.draw.circle(self.screen2, (0, 150, 255), (x, y), 5)
            self.points.append((x, y))

    def draw_lines(self):
        for i, start_point in enumerate(self.points):
            target_point = (i * self.factor) % self.section
            target_x = int(self.centre_x + self.radius * cos(self.angle * target_point + pi))
            target_y = int(self.centre_y + self.radius * sin(self.angle * target_point + pi))
            self.color.hsva = (360 / self.section * i, 100, 100)

            # r = random.randint(0, 255)
            # g = random.randint(0, 255)
            # b = random.randint(0, 255)
            pg.draw.line(self.screen, self.color, start_point, (target_x, target_y),2)

    def game_loop(self):

        self.setup()
        self.draw()
        
        go_on = True
        while go_on:
            self.screen3 = pg.font.SysFont('NotoSans', 72).render(f"{self.factor:6.1f}", False, (self.color))
            self.screen.blit(self.screen2, (0, 0))
            self.screen.blit(self.screen3, (3, 10))
            self.factor += 0.002
            self.clock.tick(30)
            for event in pg.event.get():
                if event.type == pg.QUIT or (
                    event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE
                ):
                    go_on = False

            self.draw_lines()

            pg.display.flip()

        pg.quit()


def main():
    tt = TimeTables()
    tt.game_loop()
    # print(tt.points)


if __name__ == "__main__":
    main()
