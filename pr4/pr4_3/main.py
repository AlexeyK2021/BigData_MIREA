import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.multicomp import pairwise_tukeyhsd

if __name__ == '__main__':
    data = pd.read_csv("../insurance.csv", sep=",")
    print(data.head())
    print(data.info())

    print(data["region"].unique())
    data.replace(["southeast", "northeast"], ["southwest", "northwest"], inplace=True)
    print(data["region"].unique())

    southwest = data[data["region"] == "southwest"]["bmi"]
    northwest = data[data["region"] == "northwest"]["bmi"]
    print("Scipy library: \n\t" + str(stats.f_oneway(southwest,
                                                     northwest)))  # pvalue = 2,91*10^-18 < 0,05 => присутствует различие; фактор региона оказывает влияение на ИМТ

    print("Statsmodels library:")
    # print(southwest, northwest)
    fixed_data = data[["region", "bmi"]].replace(["southwest", "northwest"], [1, 2])
    model = ols("bmi ~ region", data=fixed_data).fit()
    anova_res = sm.stats.anova_lm(model, type=2)
    print(anova_res)

    print("southwest-northwest")  # ????????
    print(stats.ttest_ind(southwest, northwest))

    tukey = pairwise_tukeyhsd(endog=data["age"], groups=data["region"], alpha=0.05)
    tukey.plot_simultaneous()
    # plt.vlines(x=49.57, ymin=-0.5, ymax=4.5, color="red")
    print(tukey.summary())
    plt.show()
