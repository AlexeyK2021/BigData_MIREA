from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn import preprocessing

if __name__ == '__main__':
    data = pd.read_csv('../winequality-red.csv', sep=',')

    print(data.info())

    scaler = preprocessing.MinMaxScaler()
    new_data = pd.DataFrame(scaler.fit_transform(data), columns=data.columns)
    print(new_data)

    t = TSNE(n_components=2, perplexity=50, random_state=123)
    TSNE_features = t.fit_transform(new_data)
    print(TSNE_features[1:4, :])

    DATA = new_data.copy()
    DATA['x'] = TSNE_features[:, 0]
    DATA['y'] = TSNE_features[:, 1]

    fig = plt.figure()
    sns.scatterplot(x='x', y='y', data=DATA, hue=data['quality'], palette='bright')
    plt.show()
