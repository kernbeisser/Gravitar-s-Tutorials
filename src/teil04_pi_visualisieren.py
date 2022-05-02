# imports as needed
import turtle as tu
import random

def read_pi():
    with open("./data/Teil_04_1_million_digits_of_pi.txt") as f:
        pi = f.read()
    return pi

def visualize_pi(pi):
    lines = 10000

    # tu.speed(0)
    tu.tracer(False)
    tu.screensize(1800, 1200, 'black')
    tu.colormode(255)

    for n in range(lines):
        zahl = pi[n]
        rotation = int(zahl) * 36
        tu.setheading(rotation)

        r = random.randint(45, 255)
        g = random.randint(45, 255)
        b = random.randint(45, 255)
        tu.pencolor((r, g, b))

        tu.forward(7)

    tu.done()

def main():
    pi = read_pi()
    # print(f"{pi[:10]}")

    visualize_pi(pi)

if __name__ == '__main__':
    main()
