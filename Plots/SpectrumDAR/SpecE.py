# This code plots the spectrum of particles emitted in pion DAR
# author: P. Chimenti, R.Bassi

from SterileDar import DARSpectrum
from SterileDar import constants as ct
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager

matplotlib.font_manager._rebuild()

print("Gráfico do espectro de energia dos (anti)neutrinos emitidos do decaimento em repouso do pion+")

spc = DARSpectrum.Spectra()


plt.rcParams.update({
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica"],
    "font.size": 16})

E = np.arange(0,ct.muonmass/2,0.01)


plt.title(r'Espectro dos neutrinos e antineutrinos')
plt.vlines(30, 0, 1, colors='black', label='Neutrinos Muônicos')
plt.plot(E,spc.dGdEve(E),'r',label='Neutrinos Eletrônicos')
plt.plot(E,spc.dGdEvmbar(E),'b',label='Antineutrinos Muônicos')
plt.ylim((-0.002, max(spc.dGdEvmbar(E))+0.002)) 
plt.legend(prop={'size': 15})
plt.grid(True)
plt.xlabel(r"Energia do (Anti)Neutrino [MeV]")
plt.ylabel(r"dN/dE [MeV$^{-1}$]")
#plt.savefig('SpecE.pdf')
plt.show()