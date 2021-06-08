#coding=utf-8
print("Gráfico da probabilidade de oscilação do neutrino do muon para o elétron para distância fixa")
import sys
sys.path.append("..")
from SterileDar import OscillationModel
import matplotlib.pyplot as plt
import numpy as np
from SterileDar import constants as ct

model = OscillationModel.OscillationModel()

E = np.arange(10e-15,100,0.01)

L = float(input('Digite um valor fixo para a distância: '))

plt.plot(E,model.Pme(L,E,ct.Ue4_2,ct.Umu4_2,ct.DelM2))
plt.title(r'Oscilação do neutrino do muon para o neutrino do elétron com L={0}m'.format(L))
plt.grid(True)
plt.xlabel(r'Energia [MeV]')
#plt.savefig('ueLfix.py')
plt.ylabel(r'Probabilidade de oscilação')

plt.show()

