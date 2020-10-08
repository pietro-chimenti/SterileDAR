# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
from SterileDar import constants as ct
from SterileDar import crosssections
import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt
import matplotlib as mpl


cs=crosssections.crosssections()


Enu= np.arange(ct.energythresholdIBD,ct.muonmass/2,.5)

print(cs.sigmatot(Enu))
plt.plot(Enu,cs.sigmatot(Enu),'r')
plt.grid(True)
plt.xlabel(u"Energia dos neutrinos [MeV]")
plt.ylabel(u"Seção de choque[MeV * m²]")
plt.show()