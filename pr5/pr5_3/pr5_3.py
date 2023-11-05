import pandas as pd
from sklearn.model_selection import train_test_split

if __name__ == '__main__':
    data = pd.read_csv("../winequality-red.csv", sep=",")
    target = data["quality"]
    x_train, x_test, y_train, y_test = train_test_split(data, target, train_size=0.8, shuffle=True, random_state=123)
    print(f"Размер для обучающей выборки:{x_train.shape}")
    print(f"Размер для признаков тестовой выборки:{x_test.shape}")
    print(f"Размер для целевого показателя обучающей выборки:{y_train.shape}")
    print(f"Размер для показателя тестовой выборки:{y_test.shape}")

