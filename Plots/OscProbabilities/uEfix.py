# This code plots the survival probability of muon neutrinos with fixed energy
# author: P. Chimenti, R.Bassi

from SterileDar import OscillationModel
import matplotlib.pyplot as plt
from SterileDar import constants as ct
import numpy as np

print("Gráfico da probabilidade de sobrevivência do neutrino do múon para energia fixa")

model = OscillationModel.OscillationModel()


plt.rcParams.update({
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica"],
    "font.size": 16,
    "axes.titlepad": 25})

L = np.arange(0,ct.Ljsns2,0.01)
E = float(input('Digite um valor fixo para a energia: '))

plt.plot(L,model.Pmm(L,E,ct.Umu4_2,ct.DelM2),'r')
plt.title(r'Sobrevivência do neutrino do múon para E={0}MeV'.format(E))
plt.grid(True)
#plt.savefig('uEfix.pdf')
plt.xlabel(r'Distância [m]')
plt.ylabel(r'Probabilidade de sobrevivência')
plt.show()