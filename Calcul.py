from matplotlib import pyplot as plt
from math import *


def calcul(puissance, prixDuKwh, prixAchat, dureeUtilisation, nbHeuresJour):
    return prixAchat + (365.25 * dureeUtilisation * puissance * nbHeuresJour * prixDuKwh)


plt.style.use("seaborn")
x_2080ti = range(0, 10)
y_2080ti = [calcul(0.21, 0.1557, 390, n, 12) for n in x_2080ti]

x_3070 = range(0, 10)
y_3070 = [calcul(0.168, 0.1557, 510, n, 12) for n in x_3070]

plt.plot(x_2080ti, y_2080ti, label="2080ti")
plt.plot(x_3070, y_3070, label="3070")

plt.xlabel("Nombre d'années")
plt.ylabel("Coût en €")
plt.title(label="Coût d'une carte graphique en fonction du prix d'achat et de la consommation pendant 12h/jour. ", fontsize=11)
plt.legend()
plt.tight_layout()
plt.show()
