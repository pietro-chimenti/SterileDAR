#Flux as function of energy from each resulting neutrino at 24m

from SterileDar import DARSpectrum
from SterileDar import OscillationModel
from SterileDar import expdata as exp
from SterileDar import constants as ct
import numpy as np


spc = DARSpectrum.Spectra()
model = OscillationModel.OscillationModel()


class Flux:
        def __init__(self, *args, **kwargs):
        # you can add additional code here if needed
                pass

#Flux of electron neutrinos that survived (N/m^2) at 24m
        def Fluxve(self,L,E,Ue4_2,DelM2):
                return ( (exp.estimatednumber*( spc.dGdEve(E)*model.Pee(L,E,Ue4_2,DelM2))) / (4*np.pi*(exp.Ljsns2)**2) )
            
#Number of electron neutrinos that oscillated from muon neutrinos (N/m^2) at 24m
        nvevmu = ( (exp.estimatednumber*(1*model.Pme(ct.Ljsns2,ct.NuMuenergy,ct.Ue4_2,ct.Umu4_2,ct.DelM2))) / (4*np.pi*(ct.Ljsns2)**2) )

#Flux of Muon neutrinos that oscillated from electron neutrinos (N/m^2) at 24m
        def Fluxvm(self,L,E,Ue4_2,Umu4_2,DelM2):
                return ( (exp.estimatednumber*(spc.dGdEve(E)*model.Pme(L,E,Ue4_2,Umu4_2,DelM2)) ) / (4*np.pi*(exp.Ljsns2)**2) )

#Flux of Muon neutrinos that survived (N/m^2) at 24m
        nvmuvmu = ( (exp.estimatednumber*(1*model.Pmm(ct.Ljsns2,ct.NuMuenergy,ct.Umu4_2,ct.DelM2))) / (4*np.pi*(ct.Ljsns2)**2) )


#Flux of tau neutrinos that oscillated from electron neutrinos (N/m^2) at 24m
        def Fluxvt(self,L,E,Ue4_2,Ut4_2,DelM2):
                return ( (exp.estimatednumber*( spc.dGdEve(E)*model.Pet(L,E,Ue4_2,Ut4_2,DelM2)) ) / (4*np.pi*(exp.Ljsns2)**2))

#Flux of tau neutrinos that oscillated from muon neutrinos (N/m^2) at 24m
        nvtauvmu = ( (exp.estimatednumber*(1*model.Pmt(ct.Ljsns2,ct.NuMuenergy,ct.Umu4_2,ct.Ut4_2,ct.DelM2))) / (4*np.pi*(ct.Ljsns2)**2) )


#Flux of antineutrinos

        def Fluxvmbar(self,L,E,Umu4_2,DelM2):
                return ((exp.estimatednumber*(spc.dGdEvmbar(E)*model.Pmm(L,E,Umu4_2,DelM2))) / (4*np.pi*(exp.Ljsns2)**2))

        def Fluxvebar(self,L,E,Ue4_2,Umu4_2,DelM2):
                return ((exp.estimatednumber*(spc.dGdEvmbar(E)*model.Pme(L,E,Ue4_2,Umu4_2,DelM2))) / (4*np.pi*(exp.Ljsns2)**2))

        def Fluxvtbar(self,L,E,Umu4_2,Ut4_2,DelM2):
                return ((exp.estimatednumber*(spc.dGdEvmbar(E)*model.Pmt(L,E,Umu4_2,Ut4_2,DelM2))) / (4*np.pi*(exp.Ljsns2)**2))