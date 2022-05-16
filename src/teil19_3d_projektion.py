# imports as needed
import pygame as pg
import numpy as np
from math import cos, sin

import logging
logging.basicConfig(level=logging.DEBUG)

cube = np.array(
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

scale = 100
translate =[400, 300, 300]

def rotate(objekt, angles):
    ax, ay, az = np.radians(angles)
    if ax:
        m_rotate = np.array([[1, 0, 0], [0, cos(ax), -sin(ax)], [0, sin(ax), cos(ax)]])
        objekt = np.matmul(objekt, m_rotate)
    if ay:
        m_rotate = np.array([[cos(ay), 0, sin(ay)], [0, 1, 0], [-sin(ay), 0, cos(ay)]])
        objekt = np.matmul(objekt, m_rotate)
    if az:
        m_rotate = np.array([[cos(az), -sin(az), 0], [sin(az), cos(az), 0], [0, 0, 1]])
        objekt = np.matmul(objekt, m_rotate)

    return objekt


# def setup():
    # WINDOW = [800, 600]
    # pg.init()
    # screen = pg.display.set_mode(WINDOW)

    # return screen


# def game_loop(screen):
def game_loop():

    global cube

    WINDOW = [800, 600]
    pg.init()
    screen = pg.display.set_mode(WINDOW)

    go_on = True

    clock = pg.time.Clock()
    ax = ay = az = 0.0

    while go_on:
        clock.tick(80)
        screen.fill((0, 0, 0))
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                go_on = False
            # if event.type == pg.KEYDOWN:
                # if event.key == pg.K_x:
                    # ax += 0.1
                # if event.key == pg.K_y:
                    # ay += 0.1
                # if event.key == pg.K_z:
                    # az += 0.1

        cube_rotated = rotate(cube, [ax,ay,az])

        projection2d = list()

        for point in cube_rotated:
            projection2d.append(point * scale + translate)

        for position in projection2d:
            pg.draw.circle(screen, (255,0,0), position[:2], 5)
            ax += 0.05
            ay += 0.05
            az += 0.05

        # logging.debug(point)
        pg.display.flip()

    pg.quit()


def main():
    # screen = setup()
    game_loop()


if __name__ == '__main__':
    main()
