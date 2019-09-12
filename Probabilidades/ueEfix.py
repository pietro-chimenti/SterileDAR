#coding=utf-8
print("Gráfico da probabilidade de oscilação do neutrino do muon para o neutrino do elétron a energia fixa")
import sys
sys.path.append("..")
from SterileDar import OscillationModel
import matplotlib.pyplot as plt
import numpy as np
import math

model = OscillationModel.OscillationModel()

L = np.arange(0,100,0.01)

E = float(input('Digite um valor fixo para a energia: '))

plt.plot(L,model.Pme(L,E))
plt.title('Oscilação do neutrino do muon para o neutrino do elétron com E={0}MeV'.format(E))
plt.grid(True)
plt.xlabel("Distância [m]")
plt.ylabel("Probabilidade de oscilação")
#plt.savefig('ueEfix.pdf')
plt.show()


