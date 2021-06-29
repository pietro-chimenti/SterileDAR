#Survival and oscillation probabilities

import numpy as np
from SterileDar import constants as ct

class OscillationModel:
    def __init__(self, *args, **kwargs):
	# you can add additional code here if needed
        pass
    
    #DelM2 = 1.7 # electron volts
    #Ue4_2   = 0.019
    #Umu4_2  = 0.015
    #Ut4_2	= 0.01
    
    def Pee(self,L,E,Ue4_2,DelM2):
        return 1.-4.*(1-Ue4_2)*(Ue4_2)*((np.sin(ct.neutrinoprobabilityconstant*DelM2*L/E))**2)
    
    def Pmm(self,L,E,Umu4_2,DelM2):
        return 1.-4.*(1-Umu4_2)*(Umu4_2)*((np.sin(ct.neutrinoprobabilityconstant*DelM2*L/E))**2)
    
    def Pme(self,L,E,Ue4_2,Umu4_2,DelM2):
        return 4.*(Umu4_2)*(Ue4_2)*((np.sin(ct.neutrinoprobabilityconstant*DelM2*L/E))**2)
    
    def Pmt(self,L,E,Umu4_2,Ut4_2,DelM2):
        return 4.*(Umu4_2)*(Ut4_2)*((np.sin(ct.neutrinoprobabilityconstant*DelM2*L/E))**2)
    
    def Pet(self,L,E,Ue4_2,Ut4_2,DelM2):
        return 4.*(Ue4_2)*(Ut4_2)*((np.sin(ct.neutrinoprobabilityconstant*DelM2*L/E))**2)