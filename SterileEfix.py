import matplotlib.pyplot as plt
import numpy as np
import math

DelM2 = 1.0
Ue4   = 0.2
Umu4  = 0.3

def Pee(x,y):
	return 1.-(4.*(1-Ue4**2)*(Ue4**2)*((np.sin((1.27)*(DelM2)*(x/y)))**2))
        
L = np.arange(50)

E = float(input('Digite um valor fixo para a energia: '))

plt.plot(L,Pee(L,E))

plt.grid(True)
plt.xlabel("Distância")
plt.ylabel("Probabilidade de oscilação")

plt.show()


