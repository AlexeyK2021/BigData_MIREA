import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    street = np.array([80, 98, 75, 91, 78])
    garage = np.array([100, 82, 105, 89, 102])

    print("Корреляция: "+str(np.corrcoef(street, garage)[0, 1]))

    plt.grid(True)
    plt.title("Диаграмма рассеяния", fontsize=20)
    plt.xlabel("Число машин на улице")
    plt.ylabel("Число машин в гараже")
    plt.scatter(street, garage, marker="o", color='crimson')
    plt.show()
