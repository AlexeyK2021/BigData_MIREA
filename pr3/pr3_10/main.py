import numpy as np
import pandas as pd

if __name__ == '__main__':
    data = pd.read_csv("../ECDCCases.csv", sep=",")

    print(data[data.notnull()].count().sort_values(ascending=False))
    all = data.notnull().sum().sum()
    void = data.isnull().sum().sum()
    void_perc = void / all * 100
    print(f"Пустых значений: {void_perc}%")

    data = data.drop(["geoId", "Cumulative_number_for_14_days_of_COVID-19_cases_per_100000"], axis=1)
    print(data[data.notnull()].count().sort_values(ascending=False))

    data["countryterritoryCode"].fillna("OTHER", inplace=True)

    med = np.median(data[data["popData2019"].notnull()].get("popData2019"))
    # print(med)
    data["popData2019"].fillna(med, inplace=True)
    print(data[data.notnull()].count().sort_values(ascending=False))
