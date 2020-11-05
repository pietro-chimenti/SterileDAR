# coding=utf-8
import sys
sys.path.append("..")
from SterileDar import Spectra
from SterileDar import Oscspec
from SterileDar import constants as ct
import matplotlib.pyplot as plt
import numpy as np

print("Gráfico do espectro de energia dos (anti)neutrinos emitidos do decaimento em repouso do pion+")

spc = Spectra.Spectra()
oscs = Oscspec.Oscspec()

E = np.arange(10e-20,52.85,0.01)

plt.title(r'Espectro dos neutrinos e neutrinos oscilados')
plt.plot(E,spc.dGdEve(E),'r',linewidth=1.0,label='Neutrinos do elétron')
plt.plot(E,oscs.Oscspecve(100,E,ct.Ue4_2,ct.Umu4_2,ct.DelM2),'b',linewidth=1.0,label= 'Neutrinos oscilados')
plt.legend()
plt.grid(True)
plt.xlabel(r'Energia do (Anti)Neutrino [MeV]')
plt.ylabel(r'dN/dE [$MeV^{-1}$]')
#plt.savefig('SpecE.pdf')
plt.show()


