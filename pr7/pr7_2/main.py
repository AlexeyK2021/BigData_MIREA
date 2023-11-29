import time

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score, r2_score
from sklearn import tree
from sklearn.model_selection import train_test_split, GridSearchCV

if __name__ == '__main__':
    data = pd.read_csv("../winequality-red.csv", sep=",")
    x = data.drop("quality", axis=1)
    y = data["quality"]

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=111)

    # param_grid = {
    #     'max_depth': [12, 18],
    #     'min_samples_split': [3, 10],
    #     'min_samples_leaf': [6, 12]
    # }
    #
    # grid_clf = GridSearchCV(RandomForestClassifier(), param_grid, scoring="f1_macro", cv=4)
    # grid_clf.fit(x_train, y_train)
    # grid_accuracy = grid_clf.score(x_test, y_test)
    # best_model = grid_clf.best_estimator_
    # print(best_model)
    #
    # start_time = time.time()
    # best_model.fit(x_train, y_train)
    # bag_accuracy = best_model.score(x_test, y_test)
    # bag_pred = best_model.predict(x_test)
    # bag_time = time.time() - start_time
    # print("Time: ", bag_time)
    # print("Accuracy: ", bag_accuracy)
    #
    # bag_f1_train = f1_score(y_train, best_model.predict(x_train), average="macro")
    # bag_f1_test = f1_score(y_test, bag_pred, average="macro")
    # print("Bagging F1 Score (Train): ", bag_f1_train)
    # print("Bagging F1 Score (Test): ", bag_f1_test)

    start_time = time.time()
    dtree = tree.DecisionTreeRegressor(random_state=111)
    dtree.fit(x_train, y_train)
    y_pred = dtree.predict(x_test)
    bag_time = time.time() - start_time

    mean_pred = np.array(y_pred)
    # bag_f1_test = f1_score(y_test, y_pred=y_pred, average="macro")
    print("Time: ", bag_time)
    # print("Bagging F1 Score (Test): ", bag_f1_test)
    print("Bagging R2 Score (Test): ", r2_score(y_test, mean_pred))

    print()
    start_time = time.time()
    modeltree = tree.DecisionTreeRegressor(max_depth=8, random_state=111)
    onemodel = modeltree.fit(x_train, y_train)
    one_pred = onemodel.predict(x_test)
    one_bag_time = time.time() - start_time

    print("One tree Time: ", one_bag_time)
    # print("One tree bagging F1 Score (Test): ", one_bag_f1_test)
    print("One tree bagging R2 Score (Test): ", r2_score(y_test, one_pred))
