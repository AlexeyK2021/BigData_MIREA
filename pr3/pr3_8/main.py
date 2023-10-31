# Нулевая гипотеза №1 -- ИМТ зависит от возраста; Альтернативная -- ИМТ не зависит от возраста
# Нулевая гипотеза №2 -- Расходы зависят от курения; Альтернативная -- Расходы не зависят от курения

import pandas as pd
from matplotlib import pyplot as plt
from scipy.stats import kstest, probplot

if __name__ == '__main__':
    data = pd.read_csv("../insurance.csv", sep=",")

    ks_test_bmi = kstest(data["bmi"], 'norm')
    print(f"BMI: {ks_test_bmi}")

    ks_test_charges = kstest(data["charges"], 'norm')
    print(f"Charges: {ks_test_charges}")

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