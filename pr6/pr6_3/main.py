import pandas as pd
from sklearn.cluster import AgglomerativeClustering
import plotly.graph_objs as go


if __name__ == '__main__':
    data = pd.read_csv("../marketing_campaign.csv", sep="\t")
    data = data.dropna()
    data = data.drop(["Education", "Marital_Status", "ID", "Dt_Customer"], axis=1)
    model2 = AgglomerativeClustering(n_clusters=6, compute_distances=True)
    clustering = model2.fit(data)
    data["Cluster"] = clustering.labels_

    fig = go.Figure(data=[go.Scatter(x=data["MntWines"],
                                     y=data["Income"],
                                     mode="markers",
                                     marker_color=data["Cluster"]
                                     )])
    fig.update_layout(xaxis_title="Amount spent on wine in last 2 years",
                      yaxis_title="Customer's yearly household income")
    fig.show()
