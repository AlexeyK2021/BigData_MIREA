import pandas as pd
import plotly as plt
from collections import Counter


def print_info(data):
    print(data.head())
    print(data.info())


def delete_nulls(data):
    return data[
        data["Name"].notnull() &
        data["Age"].notnull() &
        data["Height"].notnull() &
        data["Weight"].notnull() &
        data["Team"].notnull() &
        data["NOC"].notnull() &
        data["Games"].notnull() &
        data["Year"].notnull() &
        data["Season"].notnull() &
        data["City"].notnull() &
        data["Sport"].notnull() &
        data["Event"].notnull()
        ]


if __name__ == '__main__':
    data = pd.read_csv('../dataset_olympics.csv', sep=",")
    # print_info(data)

    print("Всего строк: " + str(len(data)))
    new_data = delete_nulls(data)
    print("Количество подходящих строк: "+str(len(new_data)))
