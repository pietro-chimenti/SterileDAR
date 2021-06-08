# coding=utf-8
import sys
sys.path.append("..")
from SterileDar import Spectra
import matplotlib.pyplot as plt
import numpy as np

print("Gráfico do espectro dos neutrinos emitidos no DAR do pion+")

spc = Spectra.Spectra()

E = np.arange(0,52.85,0.01)

plt.plot(E,spc.dGdEve(E))
plt.title(r'Espectro dos neutrinos emitidos')
plt.grid(True)
plt.xlabel(r"Energia dos neutrinos [$MeV$]")
plt.ylabel(r"dN/dE [$MeV^{-1}$]")
#plt.savefig('SpecEve.pdf')
plt.show()

