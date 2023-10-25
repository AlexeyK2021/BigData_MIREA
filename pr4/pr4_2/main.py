import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def correct_nulls(data):
    return data[
        data["price"].notnull() &
        data["battery_capacity"].notnull()
        ]


if __name__ == '__main__':
    data = pd.read_csv("../smartphones.csv", sep=",")
    data = data.drop(["brand_name", "model", "fast_charging", "processor_brand", "os"], axis=1)
    data = data.dropna()

    # price = data["price"]
    # battery = data["battery_capacity"]
    #
    # corr = battery.corr(price)
    # print("Значение корреляции ёмкости батареи к цене телефона: " + str(corr))
    #
    # plt.grid(1)
    # plt.title("Стоимость и ёмкость батареи", fontsize=20)
    # plt.xlabel("Ёмкость бюатареи в мАч")
    # plt.ylabel("Стоимость в $")
    # plt.xticks(size=9)
    # plt.yticks(size=9)
    #
    # plt.scatter(battery, price, color='crimson', alpha=0.3)
    # plt.show()

    corr = data.corr().round(3)
    # plt.matshow(corr)
    # plt.colorbar()
    sns.heatmap(corr)
    plt.savefig("test",bbox_inches='tight')
    plt.show()

    print(corr)
