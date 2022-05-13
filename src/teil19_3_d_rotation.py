# imports as needed
import pygame as pg
import numpy as np

import logging
logging.basicConfig(level=logging.DEBUG)


class ClassName:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.screen = None
        self.clock = None
        self.cube = np.array(
            [
                [-1, -1, -1],
                [1, -1, -1],
                [1, 1, -1],
                [-1, 1, -1],
                [-1, -1, 1],
                [1, -1, 1],
                [1, 1, 1],
                [-1, 1, 1],
            ]
        )

        self.ax = self.ay = self.az = 0.2
        self.scale = 100
        self.translate =[400, 300, 300]
        self.screen = None

    def setup(self):
        pg.init()
        self.screen = pg.display.set_mode((self.width, self.height))
        self.clock = pg.time.Clock()

    def rotatate(self, cube, angles):
        # angles = np.array(angles)
        ax, ay, az = np.radians(angles)
        if ax:
            rx_matrix = np.array(
                # [[1, 0, 0], [0, np.cos(ax), -np.sin(ax)], [0, np.sin(ax), np.cos(ax)]]
                np.array([[1, 0, 0], [0, np.cos(ax), -np.sin(ax)], [0, np.sin(ax), np.cos(ax)]])
            )
            cube = np.matmul(cube, rx_matrix)

        if ay:
            ry_matrix = np.array(
                # [[np.cos(ay), 0, np.sin(ay)], [0, 1, 0], [-np.sin(ay), 0, np.cos(ay)]]
                np.array([[np.cos(ay), 0, np.sin(ay)], [0, 1, 0], [-np.sin(ay), 0, np.cos(ay)]])
            )
            cube = np.matmul(cube, ry_matrix)

        if az:
            rz_matrix = np.array(
                # [[np.cos(az), -np.sin(az), 0], [-np.sin(az), np.cos(az), 0], [0, 0, 1]]
                np.array([[np.cos(az), -np.sin(az), 0], [np.sin(az), np.cos(az), 0], [0, 0, 1]])
            )
            cube = np.matmul(cube, rz_matrix)
 
        return cube


    def draw(self, angles):
        cube = self.rotatate(self.cube, angles=angles)
        for point in cube:
            point = point * self.scale + self.translate
            pg.draw.circle(self.screen, (255,0,0), point[:2], 5)

    def game_loop(self):

        ax = ay = az = 0.2
        self.setup()

        go_on = True
        while go_on:
            self.clock.tick(60)
            for event in pg.event.get():
                if event.type == pg.QUIT or (
                    event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE
                ):
                    go_on = False

            # self.draw((ax, ay, az))

            cube = self.rotatate(self.cube, angles=(ax, ay, az))
            for point in cube:
                point = point * self.scale + self.translate
                pg.draw.circle(self.screen, (255,0,0), point[:2], 5)
            
            ax += 0.1
            ay += 0.1
            az += 0.1
            
            pg.display.flip()

        pg.quit()


def main():
    cn = ClassName()
    cn.game_loop()
    # new_cube = cn.rotatate(cn.cube, (0,0,0))
    # logging.debug(new_cube)

if __name__ == "__main__":
    main()
