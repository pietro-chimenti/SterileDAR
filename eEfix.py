#coding=utf-8
from SterileDar import OscillationModel
import matplotlib.pyplot as plt
import numpy as np
import math

print("Gráfico da probabilidade de sobrevivência do neutrino do elétron para energia fixa")

model = OscillationModel.OscillationModel()

L = np.arange(0,100)

E = float(input("insira um valor para a energia ")) 

plt.plot(L,model.Pee(L,E),'r')

plt.title(u'Sobrevivência do neutrino do elétron para E={0}MeV'.format(E))
plt.grid(True)
plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.5)
plt.minorticks_on()
plt.xlabel(u"Distância [m]")
plt.ylabel(u"Probabilidade de sobrevivência")
#plt.savefig('eEfix.pdf')
plt.show()


