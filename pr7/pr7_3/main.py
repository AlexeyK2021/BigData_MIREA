import time
import pandas as pd
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split, GridSearchCV
from catboost import CatBoostClassifier

if __name__ == '__main__':
    data = pd.read_csv("../winequality-red.csv", sep=",")
    x = data.drop("quality", axis=1)
    y = data["quality"]

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.8, random_state=42)

    param_grid = {
        'max_depth': [12, 18],
        'min_samples_split': [3, 10],
        'min_samples_leaf': [6, 12]
    }

    start = time.time()
    boost_clf = CatBoostClassifier(iterations=3000, task_type='GPU', devices='0')
    boost_clf.fit(x_train, y_train)
    boost_accuracy = boost_clf.score(x_test, y_test)
    boost_pred = boost_clf.predict(x_test)
    boost_time = time.time() - start
    print("Time: ", boost_time)
    print("Accuracy: ", boost_accuracy)

    boost_f1_train = f1_score(y_train, boost_clf.predict(x_train), average="macro")
    boost_f1_test = f1_score(y_test, boost_pred, average="macro")
    print("Boosting F1 Score (Train): ", boost_f1_train)
    print("Boosting F1 Score (Test): ", boost_f1_test)
