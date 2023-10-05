import pandas as pd

if __name__ == '__main__':
    data = pd.read_csv("../ECDCCases.csv", sep=',')
    print(data.describe())

    deaths = data[data["deaths"] > 3000]
    print(deaths[["deaths", "countriesAndTerritories", "dateRep"]])