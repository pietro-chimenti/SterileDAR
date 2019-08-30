# coding=utf-8
from SterileDar import OscillationModel
import matplotlib.pyplot as plt
import numpy as np
import math

print("Gráfico da probabilidade de sobrevivência do neutrino do elétron para energia fixa")

model = OscillationModel()
model.Ue4_2 = 0.2

L = np.arange(100)

E = 30 

plt.plot(L,model.Pee(L,E))

plt.grid(True)
plt.xlabel(u"Distância")
plt.ylabel(u"Probabilidade de sobrevivência")
plt.savefig('eEfix.pdf')
#plt.show()


