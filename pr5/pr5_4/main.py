import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn
import plotly.express as px
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

if __name__ == '__main__':
    data = pd.read_csv("../winequality-red.csv", sep=",")
    predictors = data.copy().drop("quality", axis=1)
    target = data["quality"]
    x_train, x_test, y_train, y_test = train_test_split(predictors, target, train_size=0.8, shuffle=True,
                                                        random_state=123)

    print(predictors.head(5))
    print("Целевая переменная")
    print(target.head(5))

    model = LogisticRegression(random_state=123)
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    print(f"Предсказанные значения {y_pred}")
    print(f"Исходные значения {np.array(y_test)}")

    plt.rcParams["figure.figsize"] = (10, 10)
    fig = px.imshow(confusion_matrix(y_test, y_pred), text_auto=True)
    # plt.colorbar()
    fig.update_layout(xaxis_title="Target", yaxis_title="Prediction")
    fig.show()


