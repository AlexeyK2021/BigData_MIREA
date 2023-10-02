import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import rand


def make_box_plot(data):
    plt.figure(figsize=(8, 8))
    plt.boxplot(x=[
        data["age"],
        data["bmi"],
        data["children"],
        # data["charges"]
    ], vert=False, labels=["Age", "BMI", "Children"])
    plt.xticks(np.arange(0, 105, 5))
    # plt.scatter(data["age"], rand, s=1.5)
    plt.grid()
    plt.show()


if __name__ == '__main__':
    data = pd.read_csv("../insurance.csv", sep=',')
    make_box_plot(data)
