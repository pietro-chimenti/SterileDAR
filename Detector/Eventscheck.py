# -*- coding: utf-8 -*-
from SterileDar import Oscspec
from SterileDar import crosssections
from SterileDar import expdata as exp
from SterileDar import constants as ct
import numpy as np

osc = Oscspec.Oscspec()
cs = crosssections.crosssections()

nproton = float(exp.hidrogeniototal) #number of protons at the detector
npb = float(exp.pbnumber) #number of Pb atoms at the detector

class Events:
    def __init__(self, *args, **kwargs):
        # you can add additional code here if needed
        pass
    #Calculation PPO/Paraffin/LAB
    def dNdEvebar(self,E1):
        return ((nproton*exp.estimatedflux)*osc.Oscspecvebar(exp.Ljsns2,E1)*cs.sigmaIBD(E1))/(4*np.pi*exp.Ljsns2**2)
        
    #Calculation 208Pb
    def dNdEve(self,E2):
        return ((npb*exp.estimatedflux)*osc.Oscspecve1(exp.Ljsns2,E2)*(cs.sigmaPb(E2)))/(4*np.pi*exp.Ljsns2**2)


print(nproton*exp.estimatedflux)
print(osc.Oscspecvebar(exp.Ljsns2,40))
print(cs.sigmaIBD(40))
print(((nproton*exp.estimatedflux)*osc.Oscspecvebar(exp.Ljsns2,40)*cs.sigmaIBD(40))/(4*np.pi*exp.Ljsns2**2))


print(npb*exp.estimatedflux)
print(osc.Oscspecve1(exp.Ljsns2,40))
print(ct.cm2tometer2*cs.sigmaPbvee(40))
print(((npb*exp.estimatedflux)*osc.Oscspecve1(exp.Ljsns2,40)*(ct.cm2tometer2*cs.sigmaPbvee(40)))/(4*np.pi*exp.Ljsns2**2))
