import pandas as pd
import plotly as plt

COUNTRY_NUM = 30


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


# 3.6 хз как
def make_bar(countries, medals):
    fig = plt.graph_objs.Figure()
    fig.add_trace(
        plt.graph_objs.Bar(
            x=countries,
            y=medals,
            marker=dict(color=medals, coloraxis="coloraxis")
        )
    )
    fig.update_traces(marker_line_color='rgb(0,0,0)', marker_line_width=2)
    fig.update_layout(
        title=dict(
            text="Distribution of the number of medals received by different countries since 1896",
            font=dict(size=20, color='black'),
            x=0.5,
            y=1
        ),
        xaxis_title=dict(text="Country", font=dict(size=16, color='black')),
        yaxis_title=dict(text="Medal quantity", font=dict(size=16, color='black')),
        height=700,
        margin=dict(l=0, r=0, t=0, b=0)
    )
    fig.update_xaxes(tickangle=315, gridwidth=2, gridcolor='ivory')
    fig.update_yaxes(gridwidth=2, gridcolor='ivory')
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
    make_bar(countries=list(data_for_bar.keys())[:COUNTRY_NUM], medals=list(data_for_bar.values())[:COUNTRY_NUM])
