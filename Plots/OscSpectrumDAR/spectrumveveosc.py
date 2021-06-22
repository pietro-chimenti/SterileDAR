# This code plots the spectrum of particles emitted in pion DAR considering oscillation and survival probabilities
# and compares with non oscillated spectrum
# author: P. Chimenti, R.Bassi

from SterileDar import Spectra
from SterileDar import Oscspec
from SterileDar import constants as ct
import matplotlib.pyplot as plt
import numpy as np

print("Gráfico do espectro de energia dos (anti)neutrinos emitidos do decaimento em repouso do pion+")

spc = Spectra.Spectra()
oscs = Oscspec.Oscspec()

L = int(input("Digite um valor para a distância: "))

E = np.arange(10e-20,52.85,0.01)

plt.title(r'Espectro dos neutrinos e neutrinos oscilados para L={0}'.format(L))
plt.plot(E,spc.dGdEve(E),'r',linewidth=1.0,label='Neutrinos do elétron')
plt.plot(E,oscs.Oscspecve(L,E,ct.Ue4_2,ct.DelM2),'b',linewidth=1.0,label= 'Neutrinos oscilados')
plt.legend()
plt.grid(True)
plt.xlabel(r'Energia do (Anti)Neutrino [MeV]')
plt.ylabel(r'dN/dE [$MeV^{-1}$]')
#plt.savefig('SpecE.pdf')
plt.show()


