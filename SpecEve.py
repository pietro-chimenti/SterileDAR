# coding=utf-8

from SterileDar import OscillationModel
import matplotlib.pyplot as plt
import numpy as np
import math

print("Gráfico do espectro dos neutrinos emitidos no DAR do pion+")

model = OscillationModel.OscillationModel()

E = np.arange(0,52.85,0.01)

plt.plot(E,model.dGdEve(E))
plt.title(u'Espectro dos neutrinos emitidos')
plt.grid(True)
plt.xlabel(u"Energia dos neutrinos [MeV]")
plt.ylabel(u"dN/dE [MeV⁻¹]")
#plt.savefig('SpecEve.pdf')
plt.show()

