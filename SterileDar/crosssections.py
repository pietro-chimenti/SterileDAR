#Inverse beta decay cross section arxiv:9903554 equation (10)
import sys
sys.path.append("..")
from SterileDar import constants as ct
import numpy as np


f = 1
f2 = 3.706    
g = 1.26
deltainner = 0.024
sigmazero = ((((ct.planckconstantcut**2)*(ct.lightconstant**2))*((ct.fermiconstant**2) * (ct.coscabibboangle**2))*(1+deltainner))/np.pi)
delta = (ct.neutronmass - ct.protonmass)
Massnp = ((ct.neutronmass + ct.protonmass)/2)

class crosssections:
    def __init__(self, *args, **kwargs):
        # you can add additional code here if needed
        pass

    def sigmatot(self,Enu):#Cross section IBD Simple
        return sigmazero*(f**2+3*g**2)*(Enu - delta)*(np.sqrt((Enu - delta)**2 - ct.electronmass**2))
