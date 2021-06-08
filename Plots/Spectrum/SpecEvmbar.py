# coding=utf-8
import sys
sys.path.append("..")
from SterileDar import Spectra
import matplotlib.pyplot as plt
import numpy as np

print("Gráfico do espectro dos antineutrinos do muon emitidos no decaimento em repouso do pion+")

spc = Spectra.Spectra()

E = np.arange(0,52.85,0.01)

plt.plot(E,spc.dGdEvmbar(E))
plt.title(r'Espectro dos antineutrinos do muon')
plt.grid(True)
plt.xlabel(r"Energia dos antineutrinos [MeV]")
plt.ylabel(r"dN/dE [$MeV^{-1}$]")
#plt.savefig('SpecEvam.pdf')
plt.show()

