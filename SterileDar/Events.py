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
        return ((npb*exp.estimatedflux)*osc.Oscspecve1(exp.Ljsns2,E2)*(ct.cm2tometer2*cs.sigmaPbvee(E2)))/(4*np.pi*exp.Ljsns2**2)