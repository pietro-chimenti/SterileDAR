# coding=utf-8
import sys
sys.path.append("..")
from SterileDar import Spectra
import matplotlib.pyplot as plt
import numpy as np
import math

print("Gráfico do espectro de energia dos (anti)neutrinos emitidos do decaimento em repouso do pion+")

spc = Spectra.Spectra()

E = np.arange(0,52.85,0.01)

plt.title(u'Espectro dos neutrinos e antineutrinos')
plt.plot(E,spc.dGdEve(E),'r',label='Neutrinos do elétron')
plt.plot(E,spc.dGdEvmbar(E),'b',label='Antineutrinos muônicos')
plt.legend()
plt.grid(True)
plt.xlabel(u"Energia do (Anti)Neutrino [MeV]")
plt.ylabel(u"dN/dE [MeV⁻¹]")
#plt.savefig('SpecE.pdf')
plt.show()

