from math import cos, pi, sin
import pygame as pg


WIDTH = 900
HEIGHT = 600


L1 = L2 = HEIGHT // 3
angle1 = pi / 2
angle2 = pi / 2
mass1 = 10
mass2 = 9

# derivatives
angle1_1 = angle1_2 = angle2_1 = angle2_2 = 0

GRAVITY = 1.0


def calc_end_position(start_position, angle, length):
    (
        x1,
        y1,
    ) = start_position
    x2 = int(x1 + length * sin(angle))
    y2 = int(y1 + length * cos(angle))

    return x2, y2


start_possition1 = (WIDTH // 2, HEIGHT // 3)
end_position1 = calc_end_position(start_possition1, angle1, L1)

start_possition2 = end_position1
end_position2 = calc_end_position(start_possition2, angle2, L2)

old_position = end_position2


def draw(p1, p2, m):
    pg.draw.line(screen, (255, 255, 255), p1, p2, 3)
    pg.draw.circle(screen, (255, 0, 0), p2, m)


pg.init()
screen = pg.display.set_mode([WIDTH, HEIGHT])
screen2 = pg.Surface([WIDTH, HEIGHT])
# screen.fill((0, 0, 0))


def game_loop(
    angle1, angle2, mass1, mass2, angle1_1, angle1_2, angle2_1, angle2_2, old_position
):
    clock = pg.time.Clock()
    go_on = True

    while go_on:
        clock.tick(60)
        for event in pg.event.get():
            if event.type == pg.QUIT or (
                event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE
            ):
                go_on = False

        screen.blit(screen2, (0, 0))

        # monstrous formulae ...
        angle1_2 = (
            -GRAVITY * (2 * mass1 + mass2) * sin(angle1)
            - mass2 * GRAVITY * sin(angle1 - 2 * angle2)
            - 2
            * sin(angle1 - angle2)
            * mass2
            * (angle2_1**2 * L2 + angle1_1**2 * L1 * cos(angle1 - angle2))
        )

        angle1_2 = angle1_2 / (
            L1 * (2 * mass1 + mass2 - mass2 * cos(2 * angle1 - 2 * angle2))
        )

        angle2_2 = (
            2
            * sin(angle1 - angle2)
            * (
                angle1_1**2 * L1 * (mass1 + mass2)
                + GRAVITY * (mass1 + mass2) * cos(angle1)
                + angle2_1**2 * L2 * mass2 * cos(angle1 - angle2)
            )
        )
        angle2_2 = angle2_2 / (
            L2 * (2 * mass1 + mass2 - mass2 * cos(2 * angle1 - 2 * angle2))
        )

        angle1_1 += angle1_2
        angle1 += angle1_1

        angle2_1 += angle2_2
        angle2 += angle2_1

        end_position1 = calc_end_position(start_possition1, angle1, L1)

        start_possition2 = end_position1
        end_position2 = calc_end_position(start_possition2, angle2, L2)

        draw(start_possition1, end_position1, mass1)
        draw(start_possition2, end_position2, mass2)
        pg.draw.line(screen2, (0, 255, 0), old_position, end_position2, 2)
        old_position = end_position2

        pg.display.flip()

    pg.quit()


def main():
    print(f"{angle1}, {angle2}")
    print(f"\n{start_possition1}, {end_position1}")
    print(f"\n{start_possition2}, {end_position2}")

    game_loop(
        angle1,
        angle2,
        mass1,
        mass2,
        angle1_1,
        angle1_2,
        angle2_1,
        angle2_2,
        old_position,
    )


if __name__ == "__main__":
    main()
