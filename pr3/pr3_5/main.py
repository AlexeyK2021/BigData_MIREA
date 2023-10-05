import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def make_box_plot(data):
    plt.figure(figsize=(8, 8))
    # plt.boxplot(x=[
    #     data["age"],
    #     data["bmi"],
    #     data["children"],
    #     # data["charges"]
    # ], vert=False, labels=["Age", "BMI", "Children"])
    plt.subplot(411)
    plt.boxplot(data["age"], labels=["Age"], vert=False)
    plt.subplot(412)
    plt.boxplot(data["bmi"], labels=["BMI"], vert=False)
    plt.subplot(413)
    plt.boxplot(data["children"], labels=["Children"], vert=False)
    plt.subplot(414)
    plt.boxplot(data["charges"], labels=["Charges"], vert=False)
    plt.xticks(np.arange(0, 105, 5))
    # plt.scatter(data["age"], rand, s=1.5)
    plt.grid()
    plt.show()


if __name__ == '__main__':
    data = pd.read_csv("../insurance.csv", sep=',')
    make_box_plot(data)
