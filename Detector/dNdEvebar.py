# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
from SterileDar import constants as ct
from SterileDar import Oscspec
from SterileDar import crosssections
from SterileDar import expdata
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import scipy.integrate as integrate


osc = Oscspec.Oscspec()
cs = crosssections.crosssections()
exp=expdata.expdata()

Enu = np.arange(10e-20,52.85,.5) #zero to half of pion energy

n = float(exp.hidrogeniototal)

nvm = float(2.5e22) #flux for antimuon neutrinos per year

L = 24 #source-detector distance in meters


def dNdEvebar(Enu):
    return ((n*nvm)*osc.Oscspecvebar(L,Enu)*cs.sigmatot(Enu))/(4*np.pi*L**2)

x = [integrate.quad(lambda Enu: dNdEvebar(Enu), 2, 52.85)]



plt.plot(Enu,dNdEvebar(Enu),'r',linewidth=1.0)
plt.title(u'dNdEvebar para L={0}m'.format(L))
plt.grid(True)
plt.xlabel(u"Energia dos neutrinos [MeV]")
plt.ylabel(u"dN/dE [MeV⁻¹]")
plt.show()

print("Número total de Anineutrinos do elétron em um ano:{0}".format(x))


