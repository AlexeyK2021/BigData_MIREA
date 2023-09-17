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


def make_bar(countries, medals):
    fig = plt.graph_objs.Figure()
    fig.add_trace(plt.graph_objs.Bar(x=countries, y=medals))
    fig.update_layout(title="Количество медалей между командами из разных стран")
    fig.show()


if __name__ == '__main__':
    data = pd.read_csv('../dataset_olympics.csv', sep=",")

    print(len(data))
    new_data = delete_nulls(data)
    print(len(new_data))

    data_for_bar = dict()

    for index, row in new_data[new_data["Medal"].notnull()].iterrows():
        if data_for_bar.get(row['Team'], 0) == 0:
            data_for_bar[row['Team']] = 1
        else:
            data_for_bar[row['Team']] += 1
        # print(f"{row['Name']} {row['Medal']}")
    # print(data_for_bar)
    # make_bar(data_for_bar)

    # print(new_data["Team"].squeeze())
    # print(new_data[new_data["Medal"].notnull()]["Team"])
    make_bar(countries=list(data_for_bar.keys())[:25], medals=list(data_for_bar.values())[:25])
