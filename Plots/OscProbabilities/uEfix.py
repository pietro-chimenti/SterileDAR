# This code plots the survival probability of muon neutrinos with fixed energy
# author: P. Chimenti, R.Bassi

print("Gráfico da probabilidade de sobrevivência do neutrino do muon para energia fixa")

from SterileDar import OscillationModel
import matplotlib.pyplot as plt
import numpy as np
from SterileDar import constants as ct

model = OscillationModel.OscillationModel()

L = np.arange(0,100,0.01)

E = float(input('Digite um valor fixo para a energia: '))

plt.plot(L,model.Pmm(L,E,ct.Umu4_2,ct.DelM2))
plt.title(r'Sobrevivência do neutrino do muon para E={0}MeV'.format(E))
plt.grid(True)
#plt.savefig('uEfix.pdf')
plt.xlabel(r'Distância [m]')
plt.ylabel(r'Probabilidade de sobrevivência')

plt.show()

