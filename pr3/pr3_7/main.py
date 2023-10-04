from math import sqrt
import numpy as np
import pandas as pd


def conf_interval(data, z):
    std = data.std()
    avg = np.mean(data)
    se = std / sqrt(len(data))

    return [avg - z * se, avg + z * se]


if __name__ == '__main__':
    data = pd.read_csv("../insurance.csv", sep=',')

    print("Расходы:")
    left, right = conf_interval(data["charges"], 1.96)
    print(f"    Для 95% доверительного интервала: [{left}; {right}]")

    left, right = conf_interval(data["charges"], 2.58)
    print(f"    Для 99% доверительного интервала: [{left}; {right}]")

    print("Индекс массы тела:")
    left, right = conf_interval(data["bmi"], 1.96)
    print(f"    Для 95% доверительного интервала: [{left}; {right}]")

    left, right = conf_interval(data["bmi"], 2.58)
    print(f"    Для 99% доверительного интервала: [{left}; {right}]")
