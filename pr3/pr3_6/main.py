from random import randrange

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


def cpt(data, l, q):
    vals = list()
    for i in range(q):
        temp = list()
        for i in range(l):
            temp.append(data[randrange(0, len(data) - 1, 1)])
        vals.append(sum(temp) / len(temp))
    return vals


def make_hist(data, title, avg):
    plt.hist(data)
    plt.title(title)
    plt.axvline(x=avg, color="black", label="Среднее")
    plt.legend()
    plt.show()


if __name__ == '__main__':
    data = pd.read_csv("../insurance.csv", sep=',')

    for l in (1, 5, 20, 50):
        res = pd.Series(cpt(data["charges"], l, 300))
        std = res.std()

        avg = np.mean(res)
        print(f"Стандартное отклонение: {std}, Среднее арифметическое: {avg}")
        make_hist(res, f"Длина выборки: {l}", avg)
