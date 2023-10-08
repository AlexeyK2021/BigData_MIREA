import numpy as np
import pandas as pd


def correct_nulls(data):
    data = data.drop(["geoId", "Cumulative_number_for_14_days_of_COVID-19_cases_per_100000"], axis=1)

    data["countryterritoryCode"].fillna("OTHER", inplace=True)
    med = np.median(data[data["popData2019"].notnull()].get("popData2019"))
    data["popData2019"].fillna(med, inplace=True)
    return data


if __name__ == '__main__':
    data = pd.read_csv("../ECDCCases.csv", sep=',')

    data = correct_nulls(data)
    print(data.describe())

    deaths = data[data["deaths"] > 3000]
    print(deaths[["deaths", "countriesAndTerritories", "dateRep"]])
