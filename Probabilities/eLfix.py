# coding=utf-8
import sys
sys.path.append("..")
from SterileDar import OscillationModel
import matplotlib.pyplot as plt
from SterileDar import constants as ct
import numpy as np

print("Gráfico da probabilidade de sobrevivência do neutrino do elétron para distância fixa")

model = OscillationModel.OscillationModel()

E = np.arange(10e-15,100.0,0.01)

L = float(input('Digite um valor fixo para a distância: '))

plt.plot(E,model.Pee(L,E,ct.Ue4_2,ct.DelM2))
plt.title(r'Sobrevivência do neutrino do elétron para L={0}m'.format(L))
plt.grid(True)
plt.xlabel(r'Energia [MeV]')
plt.ylabel(r'Probabilidade de sobrevivência')
#plt.savefig('eLfix.pdf')
plt.show()


