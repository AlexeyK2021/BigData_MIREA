# Нулевая гипотеза №1 -- ИМТ зависит от возраста; Альтернативная -- ИМТ не зависит от возраста
# Нулевая гипотеза №2 -- Расходы зависят от курения; Альтернативная -- Расходы не зависят от курения
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from scipy.stats import kstest, probplot, norm
import seaborn

if __name__ == '__main__':
    data = pd.read_csv("../insurance.csv", sep=",")

    ks_test_bmi = kstest(data["bmi"], 'norm')
    print(f"BMI: {ks_test_bmi}")

    ks_test_charges = kstest(data["charges"], 'norm')
    print(f"Charges: {ks_test_charges}")

    # percs = np.linspace(0, 100, 21)
    # qn_a = np.percentile(a, percs)
    # qn_b = np.percentile(b, percs)

    # bmi = seaborn.jointplot(
    #     x=np.random.normal(len(bmi_data)),
    #     y=bmi_data,
    #     kind="reg",
    #     truncate=True,
    #     color="b",
    #     height=5,
    #     ratio=3,
    #     scatter_kws={"s": 10},
    #     line_kws={"lw": 1, "color": "black"}
    # )
    # plt.show()

    probplot(data["bmi"], dist="norm", plot=plt)
    plt.xlabel("Normal distribution")
    plt.ylabel("BMI distribution")
    plt.title("Probability Plot of BMI")
    plt.show()

    probplot(data["charges"], dist="norm", plot=plt)
    plt.xlabel("Normal distribution")
    plt.ylabel("Charges distribution")
    plt.title("Probability Plot of Charges")
    plt.show()
