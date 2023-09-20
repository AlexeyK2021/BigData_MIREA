import pandas as pd
from plotly import graph_objs as go

COUNTRY_NUM = 50


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


def make_pie(countries, medals):
    fig = go.Figure()
    fig.add_trace(
        go.Pie(
            labels=countries, values=medals,
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
        margin=dict(l=0, r=0, t=20, b=0)
    )
    fig.update_xaxes(tickangle=315, gridwidth=2, gridcolor='ivory', tickfont_size=14)
    fig.update_yaxes(gridwidth=2, gridcolor='ivory', tickfont_size=14)
    fig.show()


def get_data_for_bar(new_data):
    data_for_bar = dict()

    for index, row in new_data[new_data["Medal"].notnull()].iterrows():
        if data_for_bar.get(row['Team'], 0) == 0:
            data_for_bar[row['Team']] = 1
        else:
            data_for_bar[row['Team']] += 1

    medals = list(data_for_bar.values())[:COUNTRY_NUM]
    countries = list(data_for_bar.keys())[:COUNTRY_NUM]
    all_medals = sum(medals)

    new_countries_list = list()
    new_medals_list = list()

    for i in range(len(countries) - 1):
        if medals[i] / all_medals > 0.01:
            new_countries_list.append(countries[i])
            new_medals_list.append(medals[i])

    new_medals_list.append(all_medals - sum(new_medals_list))
    new_countries_list.append("Other")
    return new_countries_list, new_medals_list


if __name__ == '__main__':
    data = pd.read_csv('../dataset_olympics.csv', sep=",")

    new_data = delete_nulls(data)

    make_pie(*get_data_for_bar(new_data))
