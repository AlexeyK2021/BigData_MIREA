import pandas as pd

if __name__ == '__main__':
    data = pd.read_csv("../wine-clustering.csv", sep=",")
    print(data.info())
    print(data.head())
    print(data.isnull().sum())
    