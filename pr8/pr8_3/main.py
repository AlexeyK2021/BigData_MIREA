import time

import pandas as pd
from apriori_python import apriori

if __name__ == '__main__':
    data = pd.read_csv("../Market_Basket_Optimisation.csv")

    transactions = list()
    for i in range(data.shape[0]):
        row = data.iloc[i].dropna().tolist()
        transactions.append(row)
    # print(transactions)

    t = list()
    start = time.perf_counter()

    t1, rules = apriori(transactions, minSup=0.04, minConf=0.17)
    time1 = time.perf_counter() - start
    t.append(time1)
    print(f"Time: {time1}")
    print(*rules, sep="\n")

