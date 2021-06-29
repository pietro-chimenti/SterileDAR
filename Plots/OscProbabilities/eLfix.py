# This code plots the survival probability of electron neutrinos with a fixed distance
# author: P. Chimenti, R.Bassi

from SterileDar import OscillationModel
import matplotlib.pyplot as plt
from SterileDar import constants as ct
import numpy as np

print("Gráfico da probabilidade de sobrevivência do neutrino do elétron para distância fixa")

model = OscillationModel.OscillationModel()


plt.rcParams.update({
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica"],
    "font.size": 16,
    "axes.titlepad": 25})

E = np.arange(10e-15,ct.muonmass/2,0.01)
L = ct.Ljsns2 #float(input('Digite um valor fixo para a distância: '))

plt.plot(E,model.Pee(L,E,ct.Ue4_2,ct.DelM2),'r')
plt.title(r'Sobrevivência do neutrino do elétron para L={0}m'.format(L))
plt.grid(True)
plt.xlabel(r'Energia [MeV]')
plt.ylabel(r'Probabilidade de sobrevivência')
#plt.savefig('eLfix.pdf')
plt.show()