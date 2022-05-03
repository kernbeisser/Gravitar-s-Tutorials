# imports as needed


def get_temps():
    temps = list()
    with open("../A-beautiful-code-in-Python/Teil_08_Temperatur_Draußen Temp_2.txt", 'r') as f:
        for line in f.readlines():
            temps.append(line.strip())

    return temps


def print_temps(temps):
    for temp in temps:
        print(f"{temp}")


def main():
    temps = get_temps()
    print_temps(temps)


if __name__ == '__main__':
    main()
