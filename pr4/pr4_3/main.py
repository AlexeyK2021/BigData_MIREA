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

    southwest = data[data["region"] == "southwest"]["bmi"]
    northwest = data[data["region"] == "northwest"]["bmi"]
    southeast = data[data["region"] == "southeast"]["bmi"]
    northeast = data[data["region"] == "northeast"]["bmi"]
    print("Scipy library: \n\t" + str(stats.f_oneway(southwest, northwest, southeast, northeast)))  # pvalue = 2,91*10^-18 < 0,05 => присутствует различие; фактор региона оказывает влияение на ИМТ

    print("Statsmodels library:")
    # print(southwest, northwest)
    fixed_data = data[["region", "bmi"]]
    model = ols("bmi ~ region", data=fixed_data).fit()
    anova_res = sm.stats.anova_lm(model, type=2)
    print(anova_res)

    print()
    print("southwest-northwest")
    print(stats.ttest_ind(southwest, northwest))
    print("southwest-northeast")
    print(stats.ttest_ind(southwest, northeast))
    print("southeast-northwest")
    print(stats.ttest_ind(southeast, northwest))
    print("southeast-northeast")
    print(stats.ttest_ind(southeast, northeast))
    print("southeast-southwest")
    print(stats.ttest_ind(southeast, southwest))
    print("northwest-northeast")
    print(stats.ttest_ind(northwest, northeast))
    print()

    tukey = pairwise_tukeyhsd(endog=data["bmi"], groups=data["region"], alpha=0.05)
    tukey.plot_simultaneous()
    # plt.vlines(x=49.57, ymin=-0.5, ymax=4.5, color="red")
    print(tukey.summary())
    plt.show()  # Интервалы перекрываются => различия не существенные

    new_data = fixed_data = data[["region", "bmi", "sex"]]
    model2 = ols("bmi ~ region + sex + region:sex", data=new_data).fit()
    anova2_res = sm.stats.anova_lm(model2, typ=2)
    print(anova2_res)

    plt.figure()
    data["combination"] = data["region"] + " / " + data["sex"]
    tukey2 = pairwise_tukeyhsd(endog=data["bmi"], groups=data["combination"], alpha=0.05)
    tukey2.plot_simultaneous()
    print(tukey2.summary())
    plt.savefig("tukey2", bbox_inches='tight')
    plt.show()

