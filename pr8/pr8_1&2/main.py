import matplotlib.pyplot as plt
import pandas as pd

if __name__ == '__main__':
    data = pd.read_csv("../Market_Basket_Optimisation.csv")

    plt.figure(figsize=(10, 13))
    data.stack().value_counts(normalize=True).sort_values(ascending=False)[:20].plot(kind="bar")
    plt.savefig("diagram.png")
    plt.show()

    plt.figure(figsize=(10, 13))
    data.stack().value_counts().apply(lambda i:i/data.shape[0]).sort_values(ascending=False)[:20].plot(kind="bar")
    plt.savefig("diagram2.png")
    plt.show()
