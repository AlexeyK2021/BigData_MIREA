import pandas as pd
import umap
import seaborn as sns
from matplotlib import pyplot as plt

from sklearn import preprocessing

if __name__ == '__main__':
    data = pd.read_csv('../winequality-red.csv', sep=',')

    scaler = preprocessing.MinMaxScaler()
    new_data = pd.DataFrame(scaler.fit_transform(data), columns=data.columns)

    neighbours_num = (5, 25, 50)
    min_distance = (0.1, 0.6)

    um = dict()
    fig = plt.figure()
    DATA = new_data.copy()

    for i in range(len(neighbours_num)):
        for j in range(len(min_distance)):
            um[neighbours_num[i], min_distance[j]] = (umap.UMAP(n_neighbors=neighbours_num[i], min_dist=min_distance[j], random_state=123).fit_transform(DATA))

    sns.scatterplot(data=DATA, palette='bright')
    plt.show()
