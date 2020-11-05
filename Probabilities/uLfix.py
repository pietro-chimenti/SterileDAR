#coding=utf-8

print("Gráfico da probabilidade de sobrevivência do neutrino do muon para distância fixa")
import sys
sys.path.append("..")
import matplotlib.pyplot as plt
import numpy as np
from SterileDar import constants as ct

from SterileDar import OscillationModel

model = OscillationModel.OscillationModel()

E = np.arange(10e-15,100.0,0.01)

L = float(input('Digite um valor fixo para a distância: '))

plt.plot(E,model.Pmm(L,E,ct.Umu4_2,ct.DelM2))
plt.title('Sobrevivência do neutrino do muon para L={0}m'.format(L))
plt.grid(True)
plt.xlabel('Energia [MeV]')
plt.ylabel('Probabilidade de sobrevivência')
#plt.savefig('uLfix.pdf')
plt.show()

