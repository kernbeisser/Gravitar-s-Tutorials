# imports as needed
import pygame as pg
import numpy as np


class Teil19:
    def __init__(self):

        self.WINDOW = [800, 600]

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

        self.ax = 0.5
        self.ay = 0.5
        self.az = 0.5

        self.scale = 100
        self.translate = [400, 300]

    def rotate(self, objekt):
        ax, ay, az = np.radians([self.ax, self.ay, self.az])

        if ax:
            m_rotate = np.array(
                [[1, 0, 0], [0, np.cos(ax), -np.sin(ax)], [0, np.sin(ax), np.cos(ax)]]
            )
            objekt = np.matmul(objekt, m_rotate)
        if ay:
            m_rotate = np.array(
                [[np.cos(ay), 0, np.sin(ay)], [0, 1, 0], [-np.sin(ay), 0, np.cos(ay)]]
            )
            objekt = np.matmul(objekt, m_rotate)
        if az:
            m_rotate = np.array(
                [[np.cos(az), -np.sin(az), 0], [np.sin(az), np.cos(az), 0], [0, 0, 1]]
            )
            objekt = np.matmul(objekt, m_rotate)

        return objekt

    def game_loop(self):

        pg.init()
        self.screen = pg.display.set_mode(self.WINDOW)
        clock = pg.time.Clock()

        go_on = True
        while go_on:
            clock.tick(80)
            self.screen.fill((0, 0, 0))
            for event in pg.event.get():
                if event.type == pg.QUIT or (
                    event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE
                ):
                    go_on = False

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_x:
                        self.ax += 0.1
                    if event.key == pg.K_y:
                        self.ay += 0.1
                    if event.key == pg.K_z:
                        self.az += 0.1

            cube_rotated = self.rotate(self.cube)

            projection2d = list()

            for point in cube_rotated:
                z1 = 3 / (4 - point[2])
                persp_projection = np.array([[z1, 0, 0], [0, z1, 0], [0, 0, 1]])
                pos = np.matmul(point, persp_projection)
                pos = pos[:2]
                projection2d.append(pos * self.scale + self.translate)

            for i in range(4):
                p1 = projection2d[i]
                p2 = projection2d[(i + 1) % 4]
                p3 = projection2d[i + 4]
                p4 = projection2d[(i + 1) % 4 + 4]
                pg.draw.line(self.screen, (255, 255, 255), p1, p2, 1)
                pg.draw.line(self.screen, (255, 255, 255), p3, p4, 1)
                pg.draw.line(self.screen, (255, 255, 255), p1, p3, 1)

            for position in projection2d:
                pg.draw.circle(self.screen, (255, 0, 0), position, 5)
                self.ax += 0.1
                self.ay += 0.1
                self.az += 0.1

            pg.display.flip()

        pg.quit()


def main():
    teil19 = Teil19()
    teil19.game_loop()


if __name__ == "__main__":
    main()
