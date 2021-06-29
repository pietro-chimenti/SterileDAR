#Event numbers for neutrinos and antineutrinos considering charged current process

from SterileDar import constants as ct
from SterileDar import InteractionSpectrum
import numpy as np
import scipy.integrate as integrate

evt = InteractionSpectrum.Events()
Enu = np.arange(ct.energythresholdIBD,ct.muonmass/2,.2)
EnuPb = np.arange(5,ct.muonmass/2,.2)

int_err = 0.01
lead_min_e = 5

class EventsnumberCC:
    
#Considering PPO/Paraffin/LAB (appearance)
    def ntotalvebar(self,Ue4_2,Umu4_2,DelM2):
        return [integrate.quad(lambda Enu: evt.dNdEvebar(Enu,Ue4_2,Umu4_2,DelM2), ct.energythresholdIBD, ct.muonmass/2)]


#Considering 208Pb (1ton) (desappearance) (charged current)
    def ntotalve(self,Ue4_2,Umu4_2,DelM2):
        return ([integrate.quad(lambda Enu1: evt.dNdEvee(Enu1,Ue4_2,DelM2), lead_min_e, ct.muonmass/2, epsabs=int_err)][0][0] + evt.NMuOriginCC(ct.NuMuenergy,Ue4_2,Umu4_2,DelM2))