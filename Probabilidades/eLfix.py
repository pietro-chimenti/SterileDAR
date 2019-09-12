# coding=utf-8
import sys
sys.path.append("..")
from SterileDar import OscillationModel
import matplotlib.pyplot as plt
import numpy as np
import math

print("Gráfico da probabilidade de sobrevivência do neutrino do elétron para distância fixa")

model = OscillationModel.OscillationModel()

E = np.arange(10e-15,100.0,0.01)

L = float(input('Digite um valor fixo para a distância: '))

plt.plot(E,model.Pee(L,E))
plt.title('Sobrevivência do neutrino do elétron para L={0}m'.format(L))
plt.grid(True)
plt.xlabel(u"Energia [MeV]")
plt.ylabel(u"Probabilidade de sobrevivência")
#plt.savefig('eLfix.pdf')
plt.show()


