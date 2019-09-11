# coding=utf-8
import sys
sys.path.append("..")
from SterileDar import Oscspec
import matplotlib.pyplot as plt
import numpy as np
import math

oscs = Oscspec.Oscspec()

print("Gráfico do espectro oscilado dos antineutrinos do muon")

L = int(input("Digite um valor para a distância: "))
E = np.arange(10e-15,52.85,0.01)

plt.plot(E,oscs.Oscspecvmbar(L,E),'r',linewidth=1.0)
plt.title(u'Espectro oscilado dos antineutrinos muônicos emitidos para L={0}m'.format(L))
plt.grid(True)
plt.xlabel(u"Energia dos antineutrinos [MeV]")
plt.ylabel(u"dN/dE [MeV⁻¹]")
plt.savefig('Oscspecvmbar{0}.pdf'.format(L))
#plt.show()

