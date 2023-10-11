import numpy as np
import pandas as pd

if __name__ == '__main__':
    data = pd.read_csv("../ECDCCases.csv", sep=",")
    print("Количество непустых строк данных в столбцах:")
    print(data[data.notnull()].count().sort_values(ascending=False))
    all = data.notnull().sum().sum()
    void = data.isnull().sum().sum()
    void_perc = void / all * 100
    print(f"\nПустых значений: {void_perc}%\n")

    data = data.drop(["geoId", "Cumulative_number_for_14_days_of_COVID-19_cases_per_100000"], axis=1)
    print("Столбцы после удаления двух с наибольшим числом пустых значений:")
    print(data[data.notnull()].count().sort_values(ascending=False))
    print()

    data["countryterritoryCode"].fillna("OTHER", inplace=True)

    med = np.median(data[data["popData2019"].notnull()].get("popData2019"))
    # print(med)
    data["popData2019"].fillna(med, inplace=True)
    print("Столбцы после заполнения:")
    print(data[data.notnull()].count().sort_values(ascending=False))
