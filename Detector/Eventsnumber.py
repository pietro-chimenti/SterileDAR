#Event numbers for neutrinos and antineutrinos
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
Enu1 = np.arange(5,ct.muonmass/2,.2)


#Considering PPO/Paraffin/LAB
ntotalvebar = [integrate.quad(lambda Enu: evt.dNdEvebar(Enu), ct.energythresholdIBD, ct.muonmass/2)]

plt.plot(Enu,evt.dNdEvebar(Enu),'r',linewidth=1.0)
plt.title(r'dNdEvebar para L={0}m'.format(exp.Ljsns2))
plt.grid(True)
plt.xlabel(r"Energia dos neutrinos [MeV]")
plt.ylabel(r'dN/dE [MeV$^{-1}$]')
plt.show()

print("Número total de interações de antineutrinos do elétron em um ano:{0}".format(ntotalvebar))

#Considering 208Pb (1ton)
ntotalve = [integrate.quad(lambda Enu1: evt.dNdEve(Enu1), 5, ct.muonmass/2)]

plt.plot(Enu1,evt.dNdEve(Enu1),'r',linewidth=1.0)
plt.title(r'dNdEvebar para L={0}m'.format(exp.Ljsns2))
plt.grid(True)
plt.xlabel(r"Energia dos neutrinos [MeV]")
plt.ylabel(r'dN/dE [MeV$^{-1}$]')
plt.show()

print("Número total de interações de antineutrinos do elétron em um ano:{0}".format(ntotalve))