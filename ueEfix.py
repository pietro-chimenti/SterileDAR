print("Gráfico da probabilidade de oscilação do neutrino do muon para o neutrino do elétron a energia fixa")

import matplotlib.pyplot as plt
import numpy as np
import math

DelM2 = 1.7
Ue4   = 0.019
Umu4  = 0.015

def Pee(x,y):
	return 4.*(Ue4)*(Umu4)*(np.sin((1.27)*(DelM2)*(x/y)))**2

L = np.arange(10000)

E = float(input('Digite um valor fixo para a energia: '))

plt.plot(L,Pee(L,E))

plt.grid(True)
plt.xlabel("Distância")
plt.ylabel("Probabilidade de oscilação")

plt.show()


