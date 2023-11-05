import matplotlib.pyplot as plt
import pandas as pd

if __name__ == '__main__':
    data = pd.read_csv("../winequality-red.csv", sep=",")
    plt.hist(x=data["quality"])
    plt.show()
