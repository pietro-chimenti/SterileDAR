#Event numbers for neutrinos and antineutrinos considering neutral current process
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

#Considering 208Pb (1ton) (neutral current electron neutrino)

ntotalveve = [integrate.quad(lambda Enu1: evt.dNdEveve(Enu1,ct.Ue4_2,ct.DelM2), lead_min_e, ct.muonmass/2, epsabs=int_err)][0][0] + evt.NMuOriginNCve(ct.NuMuenergy,ct.Ue4_2,ct.Umu4_2,ct.DelM2)



#Considering 208Pb (1ton) (neutral current muon neutrino)

ntotalvmvm = [integrate.quad(lambda Enu1: evt.dNdEvmvm(Enu1,ct.Ue4_2,ct.Umu4_2,ct.DelM2), lead_min_e, ct.muonmass/2, epsabs=int_err)][0][0] + evt.NMuOriginNCvm(ct.NuMuenergy,ct.Umu4_2,ct.DelM2)



#Considering 208Pb (1ton) (neutral current tau neutrino)

ntotalvtvt = [integrate.quad(lambda Enu1: evt.dNdEvevt(Enu1,ct.Ue4_2,ct.Ut4_2,ct.DelM2), lead_min_e, ct.muonmass/2, epsabs=int_err)][0][0] + evt.NMuOriginNCvt(ct.NuMuenergy,ct.Umu4_2,ct.Ut4_2,ct.DelM2)



#Considering 208Pb (1ton) (neutral current electron antineutrino)

ntotalvebarvebar = [integrate.quad(lambda Enu1: evt.dNdEvebarvebar(Enu1,ct.Ue4_2,ct.Umu4_2,ct.DelM2), lead_min_e, ct.muonmass/2, epsabs=int_err)][0][0]



#Considering 208Pb (1ton) (neutral current muon antineutrino)

ntotalvmbarvmbar = [integrate.quad(lambda Enu1: evt.dNdEvmbarvmbar(Enu1,ct.Umu4_2,ct.DelM2), lead_min_e, ct.muonmass/2, epsabs=int_err)][0][0]



#Considering 208Pb (1ton) (neutral current tau antineutrino)

ntotalvtbarvtbar = [integrate.quad(lambda Enu1: evt.dNdEvtbarvtbar(Enu1,ct.Umu4_2,ct.Ut4_2,ct.DelM2), lead_min_e, ct.muonmass/2, epsabs=int_err)][0][0]

