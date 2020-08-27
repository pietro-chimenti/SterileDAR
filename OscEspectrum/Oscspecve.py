# coding=utf-8
import sys
sys.path.append("..")
from SterileDar import Oscspec
import matplotlib.pyplot as plt
import numpy as np
import math

oscs = Oscspec.Oscspec()

print("Gráfico do espectro oscilado dos neutrinos emitidos no DAR do pion+")

L = int(input("Digite um valor para a distância: "))
E = np.arange(10e-15,5230.85,0.01)

plt.plot(E,oscs.Oscspecve(L,E),'r',linewidth=1.0)
plt.title(u'Espectro oscilado dos neutrinos do elétron emitidos para L={0}m'.format(L))
plt.grid(True)
plt.xlabel(u"Energia dos neutrinos [MeV]")
plt.ylabel(u"dN/dE [MeV⁻¹]")
#plt.savefig('Oscspecve{0}.pdf'.format(L))
plt.show()

