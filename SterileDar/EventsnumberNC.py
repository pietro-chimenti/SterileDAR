#Event numbers for neutrinos and antineutrinos considering neutral current process

from SterileDar import constants as ct
from SterileDar import InteractionSpectrum
import numpy as np
import scipy.integrate as integrate

evt = InteractionSpectrum.Events()


int_err = 0.01
lead_min_e = 5

Enu = np.arange(ct.energythresholdIBD,ct.muonmass/2,.2)
EnuPb = np.arange(lead_min_e,ct.muonmass/2,.2)

class EventsnumberNC:

#Considering 208Pb (1ton) (neutral current electron neutrino)
    
    def ntotalveve(self,Ue4_2,Umu4_2,DelM2):
        return [integrate.quad(lambda Enu1: evt.dNdEveve(Enu1,Ue4_2,DelM2), lead_min_e, ct.muonmass/2, epsabs=int_err)][0][0] + evt.NMuOriginNCve(ct.NuMuenergy,Ue4_2,Umu4_2,DelM2)



#Considering 208Pb (1ton) (neutral current muon neutrino)

    def ntotalvmvm(self,Ue4_2,Umu4_2,DelM2):
        return [integrate.quad(lambda Enu1: evt.dNdEvmvm(Enu1,Ue4_2,Umu4_2,DelM2), lead_min_e, ct.muonmass/2, epsabs=int_err)][0][0] + evt.NMuOriginNCvm(ct.NuMuenergy,Umu4_2,DelM2)



#Considering 208Pb (1ton) (neutral current tau neutrino)

    def ntotalvtvt(self,Ue4_2,Umu4_2,Ut4_2,DelM2):
        return [integrate.quad(lambda Enu1: evt.dNdEvevt(Enu1,Ue4_2,Ut4_2,DelM2), lead_min_e, ct.muonmass/2, epsabs=int_err)][0][0] + evt.NMuOriginNCvt(ct.NuMuenergy,Umu4_2,Ut4_2,DelM2)



#Considering 208Pb (1ton) (neutral current electron antineutrino)

    def ntotalvebarvebar(self,Ue4_2,Umu4_2,DelM2):
        return [integrate.quad(lambda Enu1: evt.dNdEvebarvebar(Enu1,Ue4_2,Umu4_2,DelM2), lead_min_e, ct.muonmass/2, epsabs=int_err)][0][0]



#Considering 208Pb (1ton) (neutral current muon antineutrino)

    def ntotalvmbarvmbar(self,Umu4_2,DelM2):
        return [integrate.quad(lambda Enu1: evt.dNdEvmbarvmbar(Enu1,Umu4_2,DelM2), lead_min_e, ct.muonmass/2, epsabs=int_err)][0][0]



#Considering 208Pb (1ton) (neutral current tau antineutrino)

    def ntotalvtbarvtbar(self,Umu4_2,Ut4_2,DelM2):
        return [integrate.quad(lambda Enu1: evt.dNdEvtbarvtbar(Enu1,Umu4_2,Ut4_2,DelM2), lead_min_e, ct.muonmass/2, epsabs=int_err)][0][0]