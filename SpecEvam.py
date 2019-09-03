# coding=utf-8

from SterileDar import OscillationModel
import matplotlib.pyplot as plt
import numpy as np
import math

print("Gráfico do espectro dos antineutrinos do muon emitidos no decaimento em repouso do pion+")

model = OscillationModel.OscillationModel()

E = np.arange(0,52.85,0.01)

plt.plot(E,model.dGdEvam(E))
plt.title(u'Espectro dos antineutrinos do muon')
plt.grid(True)
plt.xlabel(u"Energia dos antineutrinos [MeV]")
plt.ylabel(u"dN/dE [MeV⁻¹]")
#plt.savefig('SpecEvam.pdf')
plt.show()

