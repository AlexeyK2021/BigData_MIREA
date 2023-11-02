import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


def mserror(x, w1, w0, y):
    ypred = w1 * x[:, 0] + w0
    return np.sum((y - ypred) ** 2) / len(ypred)


def gr_mserror(x, w1, w0, y):
    ypred = w1 * x[:, 0] + w0
    return np.array([2 / len(x) * np.sum((y - ypred)) * (-1)])


def regression():
    epc = 0.0001
    w1 = 0
    w0 = 0

    learning_rate = 0.001
    next_w1 = w1
    next_w0 = w0

    n = 100000

    for i in range(n):
        cur_w1 = next_w1
        cur_w0 = next_w0

        next_w0 = cur_w0 - learning_rate * gr_mserror()


if __name__ == '__main__':
    data = pd.read_csv("../smartphones.csv", sep=",")
    print(data.info())
    data = data.drop(["brand_name", "model", "fast_charging", "processor_brand", "os"], axis=1)
    data = data.dropna()
    print(data.info())

    corr_price = data.corr()["price"].to_frame().round(2)
    sns.heatmap(corr_price, annot=True, linewidth=0.5, cmap="coolwarm")
    plt.savefig("test", bbox_inches='tight')
    plt.show()
    # print(corr_price)

    lin_reg = LinearRegression()
    x = data[["internal_memory"]]
    y = data["price"]
    x = np.array(x, type(float))
    y = np.array(y, type(float))
    lin_reg.fit(x, y)
    print(f"Угол наклона = {lin_reg.coef_[0]}\nКоэффициент сдвига = {lin_reg.intercept_}")

    a = lin_reg.coef_[0]
    b = lin_reg.intercept_
    y_func = a * x + b

    plt.plot(x, y_func, linewidth=2, color="r", label=f"y(x)= {a:.2f}x + {b:.2f}")
    plt.scatter(x, y_func, alpha=0.7)
    plt.grid()
    plt.xlabel("Price")
    plt.ylabel("Internal memory size")
    plt.legend()
    plt.savefig("Internal_memory-price", bbox_inches='tight')
    plt.show()
    mse = mean_squared_error(y, y_func)
    print(f"MSE = {mse}")

    # regression()
