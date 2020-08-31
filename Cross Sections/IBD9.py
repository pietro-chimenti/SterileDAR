# -*- coding: utf-8 -*-

import sys
sys.path.append("..")
from SterileDar import constants as ct
import numpy as np
import math
import scipy.integrate as integrate
import matplotlib.pyplot as plt
import matplotlib as mpl

f=1
f2 = 3.706    
g = 1.26
deltainner = 0.024
Enu= np.arange(0,52.85,.5)
sigmazero = ((((ct.planckconstantcut**2)*(ct.lightconstant**2))*((ct.fermiconstant**2) * (ct.coscabibboangle**2))*(1+deltainner))/np.pi)
delta = (ct.neutronmass - ct.protonmass)
Massnp = ((ct.neutronmass + ct.protonmass)/2)

#Eezero = Enu - delta
#pezero = np.sqrt((Enu - delta)**2 - ct.electronmass**2)
#vezero = ( np.sqrt((Enu - delta)**2 - ct.electronmass**2) )/(Enu - delta)

def sigmatot(Enu):
        return sigmazero*(f**2+3*g**2)*(Enu - delta)*(np.sqrt((Enu - delta)**2 - ct.electronmass**2))
    

plt.plot(Enu,sigmatot(Enu))
plt.show()


#plt.xlabel("Valores de ka")
#plt.ylabel("Valores da integral")

#Ee1= Eezero*(1 - (Enu/Massnp)*(1 - vezero*np.cos(theta)))

#ve1= (pe1)/(Ee1)

#pe1= np.sqrt(Ee1**2 - ct.electronmass**2)