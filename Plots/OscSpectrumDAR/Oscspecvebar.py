# This code plots the spectrum of particles emitted in pion DAR considering oscillation and survival probabilities
# author: P. Chimenti, R.Bassi

from SterileDar import Oscspec
import matplotlib.pyplot as plt
from SterileDar import constants as ct
import numpy as np

oscs = Oscspec.Oscspec()

print("Gráfico do espectro oscilado dos antineutrinos do elétron")


plt.rcParams.update({
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica"],
    "font.size": 16,
    "axes.titlepad": 25})

L = ct.Ljsns2 #int(input("Digite um valor para a distância: "))
E = np.arange(10e-15,ct.muonmass/2,0.01)

plt.plot(E,oscs.Oscspecvebar(L,E,ct.Ue4_2,ct.Umu4_2,ct.DelM2),'r',linewidth=1.5)
plt.title(r'Espectro oscilado dos antineutrinos eletrônicos emitidos para L={0}'.format(L))
plt.grid(True)
plt.xlabel(r'Energia dos antineutrinos [MeV]')
plt.ylabel(r'dN/dE [MeV$^{-1}$]')
#plt.savefig('Oscspecvebar{0}.pdf'.format(L))
plt.show()