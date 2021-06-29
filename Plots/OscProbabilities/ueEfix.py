# This code plots the oscillation probability of muon to electron neutrinos with fixed energy
# author: P. Chimenti, R.Bassi

from SterileDar import OscillationModel
import matplotlib.pyplot as plt
from SterileDar import constants as ct
import numpy as np
from textwrap3 import wrap

print("Gráfico da probabilidade de oscilação do neutrino do múon para o neutrino do elétron a energia fixa")

model = OscillationModel.OscillationModel()


plt.rcParams.update({
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica"],
    "font.size": 16,
    "axes.titlepad": 25})

L = np.arange(0,ct.Ljsns2,0.01)
E = float(input('Digite um valor fixo para a energia: '))

plt.ticklabel_format(axis='y', scilimits=(0,0))
plt.plot(L,model.Pme(L,E,ct.Ue4_2,ct.Umu4_2,ct.DelM2),'r')
plt.title('\n'.join(wrap(r'Oscilação do neutrino do múon para o neutrino do elétron com E={0}MeV'.format(E),50)))
plt.grid(True)
plt.xlabel(r'Distância [m]')
plt.ylabel(r'Probabilidade de oscilação')
#plt.savefig('ueEfix.pdf')
plt.show()