import pandas as pd
from sklearn.preprocessing import MaxAbsScaler


def normalize(data):
    scaler = MaxAbsScaler()
    scaler.fit(data)
    new_data = pd.DataFrame(scaler.transform(data), columns=data.columns)
    return new_data


if __name__ == '__main__':
    data = pd.read_csv("../marketing_campaign.csv", sep="\t")
    print(data.info())
    print(data.head())
    data = data.dropna()
    print(data.isnull().sum())

    # data = data.drop(["Education", "Marital_Status", "ID", "Dt_Customer", "Year_Birth"], axis=1)
    #
    # new_data = normalize(data)
    # 
    # print(new_data)