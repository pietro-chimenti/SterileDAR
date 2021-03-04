#Event numbers for neutrinos and antineutrinos considering charged current process
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

#Considering PPO/Paraffin/LAB (appearance)
ntotalvebar = [integrate.quad(lambda Enu: evt.dNdEvebar(Enu,ct.Ue4_2,ct.Umu4_2,ct.DelM2), ct.energythresholdIBD, ct.muonmass/2)]

plt.plot(Enu,evt.dNdEvebar(Enu,ct.Ue4_2,ct.Umu4_2,ct.DelM2),'r',linewidth=1.0)
plt.plot(Enu,evt.dNdEvebar(Enu,0.025,0.025,ct.DelM2),'b',linewidth=1.0)
plt.title(r'Espectro dos antineutrinos do elétron para L={0}m'.format(exp.Ljsns2))
plt.grid(True)
plt.xlabel(r"Energia dos neutrinos [MeV]")
plt.ylabel(r'dN/dE [MeV$^{-1}$]')
plt.show()

print("Número total de interações de antineutrinos do elétron em um ano:{0}".format(ntotalvebar))

#Considering 208Pb (1ton) (desappearance) (charged current)
ntotalve = [integrate.quad(lambda Enu1: evt.dNdEvee(Enu1,ct.Ue4_2,ct.DelM2), lead_min_e, ct.muonmass/2, epsabs=int_err)][0][0] + evt.NMuOriginCC(ct.NuMuenergy,ct.Ue4_2,ct.Umu4_2,ct.DelM2) 


plt.plot(EnuPb,evt.dNdEvee(EnuPb,ct.Ue4_2,ct.DelM2),'r',linewidth=1.0)
plt.plot(EnuPb,evt.dNdEvee(EnuPb,0,ct.DelM2),'b',linewidth=1.0)
plt.plot(EnuPb,evt.dNdEvee(EnuPb,10*ct.Ue4_2,ct.DelM2),'g',linewidth=1.0)
plt.title(r'Espectro dos neutrinos do elétron para L={0}m'.format(exp.Ljsns2))
plt.grid(True)
plt.xlabel(r"Energia dos neutrinos [MeV]")
plt.ylabel(r'dN/dE [MeV$^{-1}$]')
plt.show()

print("Número total de interações de neutrinos do elétron em um ano por corrente carregada:{0}".format(ntotalve))