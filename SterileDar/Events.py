#Spectrum formulas of particle number
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
#PPO/Paraffin/LAB (IBD process)
    def dNdEvebar(self,E1,Ue4_2,Umu4_2,DelM2):
        return ((nproton*exp.estimatedflux)*osc.Oscspecvebar(exp.Ljsns2,E1,Ue4_2,Umu4_2,DelM2)*cs.sigmaIBD(E1))/(4*np.pi*exp.Ljsns2**2)
        
#208Pb
    
#Charged current
    def dNdEvee(self,E2,Ue4_2,DelM2):
        return ((npb*exp.estimatedflux)*osc.Oscspecve(exp.Ljsns2,E2,Ue4_2,DelM2)*(ct.cm2tometer2*cs.sigmaPbvee(E2)))/(4*np.pi*exp.Ljsns2**2)
    
    def NMuOriginCC(self,E2,Ue4_2,Umu4_2,DelM2):
        return ((npb*exp.estimatedflux)*osc.NuMuNue(exp.Ljsns2,E2,Ue4_2,Umu4_2,DelM2)*(ct.cm2tometer2*cs.sigmaPbvee(E2)))/(4*np.pi*exp.Ljsns2**2)
    
#Neutral current (neutrinos)
    def dNdEveve(self,E2,Ue4_2,DelM2):
        return ((npb*exp.estimatedflux)*osc.Oscspecve(exp.Ljsns2,E2,Ue4_2,DelM2)*(ct.cm2tometer2*cs.sigmaPbvv(E2)))/(4*np.pi*exp.Ljsns2**2)
    
    def NMuOriginNCve(self,E2,Ue4_2,Umu4_2,DelM2):
        return ((npb*exp.estimatedflux)*osc.NuMuNue(exp.Ljsns2,E2,Ue4_2,Umu4_2,DelM2)*(ct.cm2tometer2*cs.sigmaPbvv(E2)))/(4*np.pi*exp.Ljsns2**2)
    
    def dNdEvmvm(self,E2,Ue4_2,Umu4_2,DelM2):
        return ((npb*exp.estimatedflux)*osc.Oscspecvm(exp.Ljsns2,E2,Ue4_2,Umu4_2,DelM2)*(ct.cm2tometer2*cs.sigmaPbvv(E2)))/(4*np.pi*exp.Ljsns2**2)
    
    def NMuOriginNCvm(self,E2,Umu4_2,DelM2):
        return ((npb*exp.estimatedflux)*osc.NuMuNuMu(exp.Ljsns2,E2,Umu4_2,DelM2)*(ct.cm2tometer2*cs.sigmaPbvv(E2)))/(4*np.pi*exp.Ljsns2**2)
    
    def dNdEvevt(self,E2,Ue4_2,Ut4_2,DelM2):
        return ((npb*exp.estimatedflux)*osc.Oscspecvt(exp.Ljsns2,E2,Ue4_2,Ut4_2,DelM2)*(ct.cm2tometer2*cs.sigmaPbvv(E2)))/(4*np.pi*exp.Ljsns2**2)
    
    def NMuOriginNCvt(self,E2,Umu4_2,Ut4_2,DelM2):
        return ((npb*exp.estimatedflux)*osc.NuMuNuTau(exp.Ljsns2,E2,Umu4_2,Ut4_2,DelM2)*(ct.cm2tometer2*cs.sigmaPbvv(E2)))/(4*np.pi*exp.Ljsns2**2)
    
    
#Neutral current (antineutrinos)

    def dNdEvebarvebar(self,E2,Ue4_2,Umu4_2,DelM2):
        return (((npb*exp.estimatedflux)*osc.Oscspecvebar(exp.Ljsns2,E2,Ue4_2,Umu4_2,DelM2)*(ct.cm2tometer2*cs.sigmaPbvbarvbar(E2)))/(4*np.pi*exp.Ljsns2**2))
    
    def dNdEvmbarvmbar(self,E2,Umu4_2,DelM2):
        return (((npb*exp.estimatedflux)*osc.Oscspecvmbar(exp.Ljsns2,E2,Umu4_2,DelM2)*(ct.cm2tometer2*cs.sigmaPbvbarvbar(E2)))/(4*np.pi*exp.Ljsns2**2))
    
    def dNdEvtbarvtbar(self,E2,Umu4_2,Ut4_2,DelM2):
        return (((npb*exp.estimatedflux)*osc.Oscspecvtbar(exp.Ljsns2,E2,Umu4_2,Ut4_2,DelM2)*(ct.cm2tometer2*cs.sigmaPbvbarvbar(E2)))/(4*np.pi*exp.Ljsns2**2))