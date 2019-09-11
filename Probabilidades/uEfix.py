#coding=utf-8

print("Gráfico da probabilidade de sobrevivência do neutrino do muon para energia fixa")
import sys
sys.path.append("..")
from SterileDar import OscillationModel
import matplotlib.pyplot as plt
import numpy as np
import math

model = OscillationModel.OscillationModel()

L = np.arange(0,100,0.01)

E = float(input('Digite um valor fixo para a energia: '))

plt.plot(L,model.Pmm(L,E))
plt.title('Sobrevivência do neutrino do muon para E={0}MeV'.format(E))
plt.grid(True)
#plt.savefig('uEfix.pdf')
plt.xlabel("Distância [m]")
plt.ylabel("Probabilidade de sobrevivência")

plt.show()

