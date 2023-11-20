import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import plotly.graph_objs as go
from sklearn.preprocessing import MaxAbsScaler


def make_plot(xvalues, yvalues, xlabel, ylabel):
    Figure()
    plt.grid()
    plt.plot(xvalues, yvalues, marker="o")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()


if __name__ == '__main__':
    data = pd.read_csv("../marketing_campaign.csv", sep="\t")
    data = data.dropna()
    data = data.drop(["Education", "Marital_Status", "ID", "Dt_Customer", "Year_Birth"], axis=1)

    models = list()
    score = list()
    silhouette_scores = list()
    for i in range(2, 11):
        model = KMeans(n_clusters=i, random_state=111, init="k-means++").fit(data)
        models.append(model)
        score.append(model.inertia_)
        silhouette_scores.append(silhouette_score(data, model.labels_))

    make_plot(range(2, 11), score, "Cluster quantity", "Score")
    make_plot(range(2, 11), silhouette_scores, "Cluster quantity", "Silhouette Score")

    model1 = KMeans(n_clusters=6, random_state=111, init="k-means++")
    model1.fit(data)
    # print(model1.cluster_centers_)
    data["Cluster"] = model1.labels_
    print(data["Cluster"].value_counts())

    fig = go.Figure(data=[go.Scatter(x=data["MntWines"],
                                     y=data["Income"],
                                     mode="markers",
                                     marker_color=data["Cluster"]
                                     )])
    fig.update_layout(xaxis_title="Amount spent on wine in last 2 years",
                      yaxis_title="Customer's yearly household income")
    fig.show()

    # fig = go.Figure(data=[go.Scatter3d(x=data["MntWines"],
    #                                    y=data["Income"],
    #                                    z=data["NumStorePurchases"],
    #                                    mode="markers",
    #                                    marker_color=data["Cluster"]
    #                                    )])
    # fig.show()

    # corr_price = data.corr()["Income"].to_frame().round(2)
    # print(corr_price)
