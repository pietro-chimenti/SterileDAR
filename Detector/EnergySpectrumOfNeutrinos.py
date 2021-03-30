#table with total information about interactions
import sys
sys.path.append("..")
import matplotlib.pyplot as plt
from SterileDar import constants as ct
from SterileDar import expdata as exp
from SterileDar import Events
import numpy as np

evt = Events.Events()
Enu = np.arange(ct.energythresholdIBD,ct.muonmass/2,.2)
EnuPb = np.arange(5,ct.muonmass/2,.2)


#Considering PPO/Paraffin/LAB (appearance)
#plt.plot(Enu,evt.dNdEvebar(Enu,ct.Ue4_2,ct.Umu4_2,ct.DelM2),'r',linewidth=1.0)
#plt.plot(Enu,evt.dNdEvebar(Enu,0.025,0.025,ct.DelM2),'b',linewidth=1.0)
#plt.title(r'(PPO/Paraffin/LAB) Espectro dos antineutrinos do elétron para L={0}m'.format(exp.Ljsns2))
#plt.grid(True)
#plt.xlabel(r"Energia dos neutrinos [MeV]")
#plt.ylabel(r'dN/dE [MeV$^{-1}$]')
#plt.show()


#Considering 208Pb (1ton) (desappearance) (charged current)

plt.plot(EnuPb,evt.dNdEvee(EnuPb,ct.Ue4_2,ct.DelM2),'r',linewidth=1.0)
plt.plot(EnuPb,evt.dNdEvee(EnuPb,0,ct.DelM2),'b',linewidth=1.0)
plt.plot(EnuPb,evt.dNdEvee(EnuPb,10*ct.Ue4_2,ct.DelM2),'g',linewidth=1.0)
plt.title(r'Espectro dos neutrinos do elétron para L={0}m'.format(exp.Ljsns2))
plt.grid(True)
plt.xlabel(r"Energia dos neutrinos [MeV]")
plt.ylabel(r'dN/dE [MeV$^{-1}$]')
plt.show()


#Considering 208Pb (1ton) (neutral current electron neutrino)

plt.plot(EnuPb,evt.dNdEveve(EnuPb,ct.Ue4_2,ct.DelM2),'r',linewidth=1.0)
plt.title(r'Espectro dos neutrinos do elétron para L={0}m'.format(exp.Ljsns2))
plt.grid(True)
plt.xlabel(r"Energia dos neutrinos [MeV]")
plt.ylabel(r'dN/dE [MeV$^{-1}$]')
plt.show()


#Considering 208Pb (1ton) (neutral current muon neutrino)

plt.plot(EnuPb,evt.dNdEvmvm(EnuPb,ct.Ue4_2,ct.Umu4_2,ct.DelM2),'r',linewidth=1.0)
plt.title(r'Espectro dos neutrinos do múon para L={0}m'.format(exp.Ljsns2))
plt.grid(True)
plt.xlabel(r"Energia dos neutrinos [MeV]")
plt.ylabel(r'dN/dE [MeV$^{-1}$]')
plt.show()


#Considering 208Pb (1ton) (neutral current tau neutrino)

plt.plot(EnuPb,evt.dNdEvevt(EnuPb,ct.Ue4_2,ct.Ut4_2,ct.DelM2),'r',linewidth=1.0)
plt.title(r'Espectro dos neutrinos do tau para L={0}m'.format(exp.Ljsns2))
plt.grid(True)
plt.xlabel(r"Energia dos neutrinos [MeV]")
plt.ylabel(r'dN/dE [MeV$^{-1}$]')
plt.show()


#Considering 208Pb (1ton) (neutral current electron antineutrino)

plt.plot(EnuPb,evt.dNdEvebarvebar(EnuPb,ct.Ue4_2,ct.Umu4_2,ct.DelM2),'b',linewidth=1.0)
plt.title(r'Espectro dos antineutrinos do elétron para L={0}m'.format(exp.Ljsns2))
plt.grid(True)
plt.xlabel(r"Energia dos antineutrinos [MeV]")
plt.ylabel(r'dN/dE [MeV$^{-1}$]')
plt.show()


#Considering 208Pb (1ton) (neutral current muon antineutrino)

plt.plot(EnuPb,evt.dNdEvmbarvmbar(EnuPb,ct.Umu4_2,ct.DelM2),'b',linewidth=1.0)
plt.title(r'Espectro dos antineutrinos do muon para L={0}m'.format(exp.Ljsns2))
plt.grid(True)
plt.xlabel(r"Energia dos antineutrinos [MeV]")
plt.ylabel(r'dN/dE [MeV$^{-1}$]')
plt.show()


#Considering 208Pb (1ton) (neutral current tau antineutrino)

plt.plot(EnuPb,evt.dNdEvtbarvtbar(EnuPb,ct.Umu4_2,ct.Ut4_2,ct.DelM2),'b',linewidth=1.0)
plt.title(r'Espectro dos antineutrinos do tau para L={0}m'.format(exp.Ljsns2))
plt.grid(True)
plt.xlabel(r"Energia dos antineutrinos [MeV]")
plt.ylabel(r'dN/dE [MeV$^{-1}$]')
plt.show()
