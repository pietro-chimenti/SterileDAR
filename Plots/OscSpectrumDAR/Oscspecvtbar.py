# This code plots the spectrum of particles emitted in pion DAR considering oscillation and survival probabilities
# author: P. Chimenti, R.Bassi

from SterileDar import Oscspec
from SterileDar import constants as ct
import matplotlib.pyplot as plt
import numpy as np

oscs = Oscspec.Oscspec()

print("Gráfico do espectro oscilado dos antineutrinos do tau")

L = int(input("Digite um valor para a distância: "))
E = np.arange(10e-15,ct.muonmass/2,0.01)

plt.plot(E,oscs.Oscspecvtbar(L,E,ct.Umu4_2,ct.Ut4_2,ct.DelM2),'r',linewidth=1.0)
plt.title(r'Espectro oscilado dos antineutrinos do tau emitidos para L={0}m'.format(L))
plt.grid(True)
plt.xlabel(r'Energia dos antineutrinos [MeV]')
plt.ylabel(r'dN/dE [$MeV^{-1}$]')
#plt.savefig('Oscspecvmbar{0}.pdf'.format(L))
plt.show()

