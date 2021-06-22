# This code plots the survival probability of electron neutrinos with fixed energy
# author: P. Chimenti, R.Bassi

from SterileDar import OscillationModel
import matplotlib.pyplot as plt
from SterileDar import constants as ct
import numpy as np


print("Gráfico da probabilidade de sobrevivência do neutrino do elétron para energia fixa")

model = OscillationModel.OscillationModel()

L = np.arange(0,100)

E = float(input("insira um valor para a energia ")) 

plt.plot(L,model.Pee(L,E,ct.Ue4_2,ct.DelM2),'r')

plt.title(r'Sobrevivência do neutrino do elétron para E={0}MeV'.format(E))
plt.grid(True)
plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.5)
plt.minorticks_on()
plt.xlabel(r'Distância [m]')
plt.ylabel(r'Probabilidade de sobrevivência')
#plt.savefig('eEfix.pdf')
plt.show()


