#Event numbers for neutrinos and antineutrinos considering charged current process
import sys
sys.path.append("..")
from SterileDar import constants as ct
from SterileDar import Events
import numpy as np
import scipy.integrate as integrate

evt = Events.Events()
Enu = np.arange(ct.energythresholdIBD,ct.muonmass/2,.2)
EnuPb = np.arange(5,ct.muonmass/2,.2)

int_err = 0.01
lead_min_e = 5

#Considering PPO/Paraffin/LAB (appearance)
ntotalvebar = [integrate.quad(lambda Enu: evt.dNdEvebar(Enu,ct.Ue4_2,ct.Umu4_2,ct.DelM2), ct.energythresholdIBD, ct.muonmass/2)]


#Considering 208Pb (1ton) (desappearance) (charged current)
ntotalve = [integrate.quad(lambda Enu1: evt.dNdEvee(Enu1,ct.Ue4_2,ct.DelM2), lead_min_e, ct.muonmass/2, epsabs=int_err)][0][0] + evt.NMuOriginCC(ct.NuMuenergy,ct.Ue4_2,ct.Umu4_2,ct.DelM2)