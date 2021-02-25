#Event numbers for neutrinos and antineutrinos considering neutral current process
import sys
sys.path.append("..")
from SterileDar import constants as ct
from SterileDar import expdata as exp
from SterileDar import Events
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate

evt = Events.Events()
Enu = np.arange(ct.energythresholdIBD,ct.muonmass/2,.2)
EnuPb = np.arange(5,ct.muonmass/2,.2)

int_err = 0.01
lead_min_e = 5

#Considering 208Pb (1ton) (neutral current electron neutrino)

ntotalvv = [integrate.quad(lambda Enu1: evt.dNdEveve(Enu1,ct.Ue4_2,ct.DelM2), lead_min_e, ct.muonmass/2, epsabs=int_err)]

plt.plot(EnuPb,evt.dNdEveve(EnuPb,ct.Ue4_2,ct.DelM2),'r',linewidth=1.0)

plt.title(r'Espectro dos neutrinos do elétron para L={0}m'.format(exp.Ljsns2))
plt.grid(True)
plt.xlabel(r"Energia dos neutrinos [MeV]")
plt.ylabel(r'dN/dE [MeV$^{-1}$]')
plt.show()

print("Número total de interações de neutrinos do elétron em um ano por corrente neutra:{0}".format(ntotalvv))

#Considering 208Pb (1ton) (neutral current electron antineutrino)

ntotalvebarvebar = [integrate.quad(lambda Enu1: evt.dNdEvebarvebar(Enu1,ct.Ue4_2,ct.Umu4_2,ct.DelM2), lead_min_e, ct.muonmass/2, epsabs=int_err)]

plt.plot(EnuPb,evt.dNdEvebarvebar(EnuPb,ct.Ue4_2,ct.Umu4_2,ct.DelM2),'b',linewidth=1.0)

plt.title(r'Espectro dos antineutrinos do elétron para L={0}m'.format(exp.Ljsns2))
plt.grid(True)
plt.xlabel(r"Energia dos antineutrinos [MeV]")
plt.ylabel(r'dN/dE [MeV$^{-1}$]')
plt.show()

print("Número total de interações de antineutrinos do elétron em um ano por corrente neutra:{0}".format(ntotalvebarvebar))