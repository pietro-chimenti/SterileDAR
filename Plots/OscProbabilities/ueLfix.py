# This code plots the oscillation probability of muon to electron neutrinos with a fixed distance
# author: P. Chimenti, R.Bassi

from SterileDar import OscillationModel
import matplotlib.pyplot as plt
from SterileDar import constants as ct
import numpy as np
from textwrap3 import wrap

print("Gráfico da probabilidade de oscilação do neutrino do múon para o elétron para distância fixa")

model = OscillationModel.OscillationModel()


plt.rcParams.update({
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica"],
    "font.size": 16,
    "axes.titlepad": 25})

E = np.arange(10e-15,ct.muonmass/2,0.01)
L = ct.Ljsns2 #float(input('Digite um valor fixo para a distância: '))

plt.plot(E,model.Pme(L,E,ct.Ue4_2,ct.Umu4_2,ct.DelM2),'r')
plt.ticklabel_format(axis='y', scilimits=(0,0))
plt.title('\n'.join(wrap(r'Oscilação do neutrino do múon para o neutrino do elétron com L={0}m'.format(L),50)))
plt.grid(True)
plt.xlabel(r'Energia [MeV]')
#plt.savefig('ueLfix.py')
plt.ylabel(r'Probabilidade de oscilação')
plt.show()