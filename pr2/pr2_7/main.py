import time

import pandas as pd
from umap import UMAP
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

    start = time.time()
    for i in range(len(neighbours_num)):
        for j in range(len(min_distance)):
            um[neighbours_num[i], min_distance[j]] = (
                UMAP(n_neighbors=neighbours_num[i], min_dist=min_distance[j], random_state=123).fit_transform(DATA))

    print("Working time = " + str(time.time() - start))
    
    DATA = new_data.copy()
    DATA['x'] = um[(5, 0.1)][:, 0]
    DATA['y'] = um[(5, 0.1)][:, 1]
    plt.title(label='neighbours_num=5; min_distance=0.1')
    sns.scatterplot(x='x', y='y', data=DATA, hue=data['quality'], palette='bright')
    plt.show()

    DATA = new_data.copy()
    DATA['x'] = um[(5, 0.6)][:, 0]
    DATA['y'] = um[(5, 0.6)][:, 1]
    plt.title(label='neighbours_num=5; min_distance=0.6')
    sns.scatterplot(x='x', y='y', data=DATA, hue=data['quality'], palette='bright')
    plt.show()

    DATA = new_data.copy()
    DATA['x'] = um[(25, 0.1)][:, 0]
    DATA['y'] = um[(25, 0.1)][:, 1]
    plt.title(label='neighbours_num=25; min_distance=0.1')
    sns.scatterplot(x='x', y='y', data=DATA, hue=data['quality'], palette='bright')
    plt.show()

    DATA = new_data.copy()
    DATA['x'] = um[(25, 0.6)][:, 0]
    DATA['y'] = um[(25, 0.6)][:, 1]
    plt.title(label='neighbours_num=25; min_distance=0.6')
    sns.scatterplot(x='x', y='y', data=DATA, hue=data['quality'], palette='bright')
    plt.show()

    DATA = new_data.copy()
    DATA['x'] = um[(50, 0.1)][:, 0]
    DATA['y'] = um[(50, 0.1)][:, 1]
    plt.title(label='neighbours_num=50; min_distance=0.1')
    sns.scatterplot(x='x', y='y', data=DATA, hue=data['quality'], palette='bright')
    plt.show()

    DATA = new_data.copy()
    DATA['x'] = um[(50, 0.6)][:, 0]
    DATA['y'] = um[(50, 0.6)][:, 1]
    plt.title(label='neighbours_num=50; min_distance=0.6')
    sns.scatterplot(x='x', y='y', data=DATA, hue=data['quality'], palette='bright')
    plt.show()
