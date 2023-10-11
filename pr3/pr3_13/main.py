import pandas as pd
import scipy.stats as sts

if __name__ == '__main__':
    data = pd.read_csv("../bmi.csv", sep=",")

    southwest = pd.to_numeric(data[data["region"] == "southwest"]["bmi"].values)
    northwest = pd.to_numeric(data[data["region"] == "northwest"]["bmi"].values)

    s_shapiro = sts.shapiro(southwest)
    print(f"Southwest Shapiro:\t{s_shapiro}")
    n_shapiro = sts.shapiro(northwest)
    print(f"Northwest Shapiro:\t{n_shapiro}")

    bartlett = sts.bartlett(southwest,northwest)
    print(f"Bartlett:\t{bartlett}")

    t_student = sts.ttest_ind(southwest, northwest)
    print(f"T-Student test: \t{t_student}")
