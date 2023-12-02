import time

import matplotlib.pyplot as plt
import pandas as pd
from apriori_python import apriori
from apyori import apriori as apriori2
from efficient_apriori import apriori as apriori3
from fpgrowth_py import fpgrowth

if __name__ == '__main__':
    data = pd.read_csv("../Market_Basket_Optimisation.csv")

    transactions = list()
    for i in range(data.shape[0]):
        row = data.iloc[i].dropna().tolist()
        transactions.append(row)
    # print(transactions)

    t = list()
    start = time.perf_counter()
    t1, rules = apriori(transactions, minSup=0.04, minConf=0.17)  # apriori_python
    time1 = time.perf_counter() - start
    t.append(time1)
    print(f"Time: {time1}")
    print(*rules, sep="\n")

    print()
    start = time.perf_counter()
    rules2 = apriori2(transactions, min_support=0.04, min_confidence=0.17, min_lift=1.0001)  # apyori
    results2 = list(rules2)
    time2 = time.perf_counter() - start
    t.append(time2)
    for res in results2:
        for sub in res[2]:
            print(sub[0], sub[1])
            print(f"Support: {res[1]}\nConfidence: {sub[2]}\nLift: {sub[3]}\n")

    start = time.perf_counter()
    items, rules3 = apriori3(transactions, min_support=0.039, min_confidence=0.17)
    time3 = time.perf_counter() - start
    t.append(time3)

    for i in range(len(rules3) - 1):
        print(f"{i + 1}. {rules3[i]}")

    print()
    start = time.perf_counter()
    items, rules4 = fpgrowth(transactions, minSupRatio=0.039, minConf=0.17)
    time4 = time.perf_counter() - start
    t.append(time4)
    for i in range(len(rules4) - 1):
        print(f"{i + 1}. {rules4[i]}")

    print(f"Время работы apriori_python:{t[0]}")
    print(f"Время работы apyori:{t[1]}")
    print(f"Время работы efficient_apriori:{t[2]}")
    print(f"Время работы fpgrowth_py:{t[3]}")

    plt.bar(["apriori_python", "apyori", "efficient_apriori", "fpgrowth_py"],t,
            label="Сравнение скорости работы алгоритмов")
    plt.show()
