# This code plots the oscillation probability of muon to electron neutrinos with fixed energy
# author: P. Chimenti, R.Bassi

print("Gráfico da probabilidade de oscilação do neutrino do muon para o neutrino do elétron a energia fixa")

from SterileDar import OscillationModel
import matplotlib.pyplot as plt
import numpy as np
from SterileDar import constants as ct

model = OscillationModel.OscillationModel()

L = np.arange(0,100,0.01)

E = float(input('Digite um valor fixo para a energia: '))

plt.plot(L,model.Pme(L,E,ct.Ue4_2,ct.Umu4_2,ct.DelM2))
plt.title(r'Oscilação do neutrino do muon para o neutrino do elétron com E={0}MeV'.format(E))
plt.grid(True)
plt.xlabel(r'Distância [m]')
plt.ylabel(r'Probabilidade de oscilação')
#plt.savefig('ueEfix.pdf')
plt.show()


