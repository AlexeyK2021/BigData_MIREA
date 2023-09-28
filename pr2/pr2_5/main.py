import pandas as pd
import matplotlib.pyplot as plt


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


def get_max_height_over_years(data):
    data_for_bar = dict()

    for year in data['Year'].unique():
        data_for_bar[year] = data[data['Year'] == year].loc[:, 'Height'].max()

    sorted_by_year = sorted(data_for_bar.items(), key=lambda x: x[0])
    sorted_by_year_dict = dict(sorted_by_year)
    return sorted_by_year_dict.keys(), sorted_by_year_dict.values()


def get_max_width_over_years(data):
    data_for_bar = dict()

    for year in data['Year'].unique():
        data_for_bar[year] = data[data['Year'] == year].loc[:, 'Weight'].max()

    sorted_by_year = sorted(data_for_bar.items(), key=lambda x: x[0])
    sorted_by_year_dict = dict(sorted_by_year)
    return sorted_by_year_dict.keys(), sorted_by_year_dict.values()


def get_participants_count_over_years(data):
    data_for_bar = dict()

    for year in data['Year'].unique():
        data_for_bar[year] = data[data['Year'] == year]['ID'].count()

    sorted_by_year = sorted(data_for_bar.items(), key=lambda x: x[0])
    sorted_by_year_dict = dict(sorted_by_year)
    return sorted_by_year_dict.keys(), sorted_by_year_dict.values()


def make_plot(year, value, plot_name, y_name, x_name='Year'):
    fig = plt.figure(plot_name)
    params = {
        'lines.markerfacecolor': 'white',
        'lines.markeredgecolor': 'black',
        'lines.marker': '.',
        'lines.markersize': 2
    }
    plt.rcParams.update(params)

    plt.plot(year, value, color='crimson')
    plt.suptitle(plot_name)
    plt.ylabel(y_name)
    plt.xlabel(x_name)
    plt.grid(visible=True, color='mistyrose', linewidth=2)
    plt.show()


if __name__ == '__main__':
    data = pd.read_csv('../dataset_olympics.csv', sep=",")

    new_data = delete_nulls(data)

    make_plot(
        *get_participants_count_over_years(new_data),
        plot_name='Dependence of the quantity of participants on the year',
        y_name='Participants quantity'
    )
    make_plot(
        *get_max_height_over_years(new_data),
        plot_name='Dependence of the maximum height of participants on the year',
        y_name='Participants maximum height'
    )
    make_plot(
        *get_max_width_over_years(new_data),
        plot_name='Dependence of the maximum weight of participants on the year',
        y_name='Participants maximum weight'
    )
