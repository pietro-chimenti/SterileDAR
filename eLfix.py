print("Gráfico da probabilidade de sobrevivência do neutrino do elétron para distância fixa")

import matplotlib.pyplot as plt
import numpy as np
import math

DelM2 = 1.7
Ue4   = 0.019
Umu4  = 0.015

def Pee(x,y):
	return 1.-(4.*(1-Ue4)*(Ue4)*((np.sin((1.27)*(DelM2)*(x/y)))**2))

E = np.arange(0.00000000000000000000000000000001,5000.0)

L = float(input('Digite um valor fixo para a distância: '))

plt.plot(E,Pee(L,E))

plt.grid(True)
plt.xlabel("Energia")
plt.ylabel("Probabilidade de sobrevivência")

plt.show()


