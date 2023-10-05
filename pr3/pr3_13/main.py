import pandas as pd

if __name__ == '__main__':
    data = pd.read_csv("../bmi.csv", sep=",")

    southwest = data[data["region" == "southwest"]]
    northwest = data[data["region" == "northwest"]]
    