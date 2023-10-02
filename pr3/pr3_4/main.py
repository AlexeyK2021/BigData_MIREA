import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as sts


def make_bmi_hist(data, title):
    moda = sts.mode(data)[0]
    med = np.median(data)
    avg = np.mean(data)

    std = data.std()
    raz = data.max() - data.min()
    iqr = np.percentile(data, 25, method="midpoint") - np.percentile(data, 75, method="midpoint")

    print("Индекс Массы тела:")
    print(f"Мода: {moda}, Медиана: {med}, Среднее: {avg}")
    print(f"Размах: {raz}, Стандартное отклонение: {std}, Межквартильный размах: {iqr}")

    plt.hist(data)
    plt.axvline(x=moda, color="red", label="Мода")
    plt.axvline(x=med, color="black", label="Медиана")
    plt.axvline(x=avg, color="orange", label="Среднее")
    plt.legend()
    plt.title(title)
    plt.show()


def make_charges_hist(data, title):
    moda = sts.mode(data)[0]
    med = np.median(data)
    avg = np.mean(data)

    std = data.std()
    raz = data.max() - data.min()
    iqr = np.percentile(data, 25, method="midpoint") - np.percentile(data, 75, method="midpoint")

    print("Расходы:")
    print(f"Мода: {moda}, Медиана: {med}, Среднее: {avg}")
    print(f"Размах: {raz}, Стандартное отклонение: {std}, Межквартильный размах: {iqr}")

    plt.hist(data)
    plt.axvline(x=moda, color="red", label="Мода")
    plt.axvline(x=med, color="black", label="Медиана")
    plt.axvline(x=avg, color="orange", label="Среднее")
    plt.legend()
    plt.title(title)
    plt.show()


if __name__ == '__main__':
    data = pd.read_csv("../insurance.csv", sep=',')

    make_bmi_hist(data["bmi"], title="Распределение по значению индекса массы тела")
    make_charges_hist(data["charges"], title="Распределение по значению расходов")
