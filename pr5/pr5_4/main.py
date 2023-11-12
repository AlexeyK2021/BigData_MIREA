import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC


def show_matrix(y_test_, y_pred_):
    global fig
    plt.rcParams["figure.figsize"] = (10, 10)
    fig = px.imshow(confusion_matrix(y_test_, y_pred_), text_auto=True)
    fig.update_layout(xaxis_title="Target", yaxis_title="Prediction")
    fig.show()


if __name__ == '__main__':
    data = pd.read_csv("../winequality-red.csv", sep=",")
    predictors = data.copy().drop("quality", axis=1)
    target = data["quality"]
    x_train, x_test, y_train, y_test = train_test_split(predictors, target, train_size=0.8, shuffle=True,
                                                        random_state=123)

    # print(predictors.head(5))
    # print("Целевая переменная")
    # print(target.head(5))

    model = LogisticRegression(random_state=123)  # Логистическая регрессия
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    print(f"Предсказанные значения {y_pred}")
    print(f"Исходные значения {np.array(y_test)}")
    print(classification_report(y_pred, y_test))
    show_matrix(y_test, y_pred)

    param_kernels = ("linear", "rbf", "poly", "sigmoid")  # SVM
    parameters = {"kernel": param_kernels}
    model = SVC()
    grid_search_svm = GridSearchCV(estimator=model, param_grid=parameters, cv=6)
    grid_search_svm.fit(x_train, y_train)
    best_model = grid_search_svm.best_estimator_
    print(f"Best model: {best_model.kernel}")
    svm_preds = best_model.predict(x_test)
    print(classification_report(svm_preds, y_test))
    show_matrix(y_test, svm_preds)

    number_of_neighbors = np.arange(3, 10)
    model_knn = KNeighborsClassifier()
    params_knn = {"n_neighbors": number_of_neighbors}
    grid_search_knn = GridSearchCV(estimator=model_knn, param_grid=params_knn, cv=6)
    grid_search_knn.fit(x_train, y_train)
    print(f"KNN Best Score: {grid_search_knn.best_score_}")
    print(f"KNN Best Estimator: {grid_search_knn.best_estimator_}")
    knn_preds = grid_search_knn.predict(x_test)
    print(classification_report(knn_preds, y_test))
    show_matrix(y_test, knn_preds)
