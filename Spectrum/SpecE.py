# coding=utf-8
import sys
sys.path.append("..")
from SterileDar import Spectra
import matplotlib.pyplot as plt
import numpy as np

print("Gráfico do espectro de energia dos (anti)neutrinos emitidos do decaimento em repouso do pion+")

spc = Spectra.Spectra()

E = np.arange(0,52.85,0.01)

plt.title(r'Espectro dos neutrinos e antineutrinos')
plt.plot(E,spc.dGdEve(E),'r',label='Neutrinos do elétron')
plt.plot(E,spc.dGdEvmbar(E),'b',label='Antineutrinos muônicos')
plt.legend()
plt.grid(True)
plt.xlabel(r"Energia do (Anti)Neutrino [$MeV$]")
plt.ylabel(r"dN/dE [$MeV^{-1}$]")
#plt.savefig('SpecE.pdf')
plt.show()

