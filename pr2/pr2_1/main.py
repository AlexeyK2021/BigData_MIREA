import pandas as pd
from plotly import graph_objs as gj


if __name__ == '__main__':
    data = pd.read_csv('../spotify_tracks_small.csv', sep=",")

    print(data.head())
    print(data.info())

    gj.Bar()
