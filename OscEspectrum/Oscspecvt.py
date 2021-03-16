# coding=utf-8
import sys
sys.path.append("..")
from SterileDar import Oscspec
import matplotlib.pyplot as plt
from SterileDar import constants as ct
import numpy as np

oscs = Oscspec.Oscspec()

print("Gráfico do espectro oscilado dos neutrinos do tau")

L = int(input("Digite um valor para a distância: "))
E = np.arange(10e-15,52.85,0.01)

plt.plot(E,oscs.Oscspecvt(L,E,ct.Ue4_2,ct.Ut4_2,ct.DelM2),'r',linewidth=1.0)
plt.title(r'Espectro oscilado dos neutrinos do tau emitidos para L={0}m'.format(L))
plt.grid(True)
plt.xlabel(r'Energia dos neutrinos [MeV]')
plt.ylabel(r'dN/dE [$MeV^{-1}$]')
#plt.savefig('Oscspecvt{0}.pdf'.format(L))
plt.show()

