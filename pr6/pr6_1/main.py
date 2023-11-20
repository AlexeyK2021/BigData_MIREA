import pandas as pd

if __name__ == '__main__':
    data = pd.read_csv("../marketing_campaign.csv", sep="\t")
    print(data.info())
    print(data.head())
    data = data.dropna()
    print(data.isnull().sum())
    