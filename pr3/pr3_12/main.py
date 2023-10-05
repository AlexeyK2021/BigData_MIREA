import pandas as pd

if __name__ == '__main__':
    data = pd.read_csv("../ECDCCases.csv", sep=',')

    duplicates = data[data.duplicated()]
    print(duplicates)
    data = data.drop_duplicates()

    duplicates = data[data.duplicated()]
    print(duplicates)
