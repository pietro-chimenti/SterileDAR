# This code plots the spectrum of particles emitted in pion DAR considering oscillation and survival probabilities
# author: P. Chimenti, R.Bassi

from SterileDar import Oscspec
import matplotlib.pyplot as plt
from SterileDar import constants as ct
import numpy as np

oscs = Oscspec.Oscspec()

print("Gráfico do espectro oscilado dos neutrinos emitidos no DAR do pion+")


plt.rcParams.update({
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica"],
    "font.size": 16,
    "axes.titlepad": 25})

L = ct.Ljsns2 #int(input("Digite um valor para a distância: "))
E = np.arange(10e-15,ct.muonmass/2,0.01)

plt.plot(E,oscs.Oscspecve(L,E,ct.Ue4_2,ct.DelM2),'r',linewidth=1.5)
plt.title(r'Espectro oscilado dos neutrinos do elétron emitidos para L={0}m'.format(L))
plt.grid(True)
plt.xlabel(r'Energia dos neutrinos [MeV]')
plt.ylabel(r'dN/dE [MeV$^{-1}$]')
#plt.savefig('Oscspecve{0}.pdf'.format(L))
plt.show()