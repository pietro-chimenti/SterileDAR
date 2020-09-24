# -*- coding: utf-8 -*-

import sys
sys.path.append("..")
from SterileDar import constants as ct
import numpy as np
import math
import scipy.integrate as integrate
import matplotlib.pyplot as plt
import matplotlib as mpl

fr = 1.7152
taun = 880.2
Enu = np.arange(ct.energythresholdIBD,ct.muonmass/2,.5)

delta = (ct.neutronmass - ct.protonmass)

Massnp = ((ct.neutronmass + ct.protonmass)/2)

#Eezero = Enu - delta
#pezero = np.sqrt((Enu - delta)**2 - ct.electronmass**2)
#vezero = ( np.sqrt((Enu - delta)**2 - ct.electronmass**2) )/(Enu - delta)

def sigmatot(Enu):
        return ((2*(np.pi**2)/(ct.electronmass**5))*(1/(fr*taun))*(Enu-delta)*(np.sqrt((Enu-delta)**2-(ct.electronmass)**2)))


plt.plot(Enu,sigmatot(Enu),'r')
plt.show()

