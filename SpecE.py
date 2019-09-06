# coding=utf-8

from SterileDar import OscillationModel
import matplotlib.pyplot as plt
import numpy as np
import math

print("Gráfico do espectro de energia dos (anti)neutrinos emitidos do decaimento em repouso do pion+")

model = OscillationModel.OscillationModel()

E = np.arange(0,52.85,0.01)

plt.title(u'Espectro dos neutrinos e antineutrinos')
plt.plot(E,model.dGdEve(E),'r',label='Neutrinos do elétron')
plt.plot(E,model.dGdEvam(E),'b',label='Antineutrinos muônicos')
plt.grid(True)
plt.xlabel(u"Energia do (Anti)Neutrino [MeV]")
plt.ylabel(u"dN/dE [MeV⁻¹]")
#plt.savefig('SpecE.pdf')
plt.show()

