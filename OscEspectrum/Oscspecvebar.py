# coding=utf-8
import sys
sys.path.append("..")
from SterileDar import Oscspec
import matplotlib.pyplot as plt
from SterileDar import constants as ct
import numpy as np
import math

oscs = Oscspec.Oscspec()

print("Gráfico do espectro oscilado dos antineutrinos do elétron")

L = int(input("Digite um valor para a distância: "))
E = np.arange(10e-15,ct.muonmass/2,0.01)

plt.plot(E,oscs.Oscspecvebar(L,E),'r',linewidth=1.0)
plt.title(u'Espectro oscilado dos antineutrinos eletrônicos emitidos para L={0}'.format(L))
plt.grid(True)
plt.xlabel(u"Energia dos antineutrinos [MeV]")
plt.ylabel(u"dN/dE [MeV⁻¹]")
plt.savefig('Oscspecvebar{0}.pdf'.format(L))
#plt.show()

