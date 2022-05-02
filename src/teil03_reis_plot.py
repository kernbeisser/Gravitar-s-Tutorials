# imports as needed
import matplotlib.pyplot as plt


def reis1():
    rk_list = [2**0]

    for feld in range(1, 65):
        rk_list.append(2**feld)

    return rk_list

def main():
    plt.plot(reis1())
    plt.show()

if __name__ == '__main__':
    main()
