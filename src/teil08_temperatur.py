"""
Gravitar's python tutorials Teil 8
"""

from cProfile import label
import matplotlib.pyplot as plt
import datetime as dt
from collections import defaultdict

def get_temps():
    """
    blah
    """
    tageswerte = defaultdict(list)

    with open("./data/Teil_08_Temperatur.txt", 'r', encoding='utf-8') as f:
        for zeile in f:
            date, temp = zeile.strip().split('\t')
            datum = dt.datetime.strptime(date, '%d.%m.%Y %H:%M:%S').date()
            temp = float(temp)
            tageswerte[datum].append(temp)
            # if datum not in tageswerte:
            #     tageswerte[datum] = [temp]
            # else:
            #     tageswerte[datum].append(temp)


    return tageswerte


def datum_max_min(tageswerte):
    max_tageswert = list()
    min_tageswert = list()
    datum_tageswert = list()

    for datum in tageswerte.keys():
        if abs(max(tageswerte[datum])) < 40 and abs(min(tageswerte[datum])) < 40:
            max_tageswert.append(max(tageswerte[datum]))
            min_tageswert.append(min(tageswerte[datum]))
            datum_tageswert.append(datum)

    return max_tageswert, min_tageswert, datum_tageswert


def plot_temps(max_tageswert, min_tageswert, datum_tageswert):
    fig, ax = plt.subplots()
    ax.plot(datum_tageswert, max_tageswert, lw=1, label='High', color='red')
    ax.plot(datum_tageswert, min_tageswert, lw=1, label='Low', color='blue')
    ax.grid(linestyle='-.', linewidth='0.5', color='green')
    ax.legend()
    plt.show()

def main():
    """
    blah
    """
    tageswerte = get_temps()
    # print(tageswerte.values())
    max_tageswert, min_tageswert, datum_tageswert = datum_max_min(tageswerte)
    plot_temps(max_tageswert, min_tageswert, datum_tageswert)



if __name__ == '__main__':
    main()
