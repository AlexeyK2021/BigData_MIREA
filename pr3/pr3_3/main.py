import pandas as pd
import matplotlib.pyplot as plt


def make_hist(data, title):
    plt.hist(data)
    plt.title(title)
    plt.show()


if __name__ == '__main__':
    data = pd.read_csv("../insurance.csv", sep=',')

    make_hist(data["age"], "Distribution by age")
    make_hist(data["bmi"], "Distribution by Body Mass Index value")
    make_hist(data["children"], "Distribution by children quantity")
    make_hist(data["charges"], "Distribution by charges value")