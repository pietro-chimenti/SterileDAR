# This code plots the spectra of particle of both neutrinos and antineutrinos as a function of energy
# CC and NC interactions
# author: P. Chimenti, R.Bassi

import matplotlib.pyplot as plt
from SterileDar import constants as ct
from SterileDar import expdata as exp
from SterileDar import InteractionSpectrum
import numpy as np
from textwrap3 import wrap

evt = InteractionSpectrum.Events()
Enu = np.arange(ct.energythresholdIBD,ct.muonmass/2,.2)
EnuPb = np.arange(ct.lead_min_e,ct.muonmass/2,.2)


plt.rcParams.update({
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica"],
    "font.size": 16,
    "axes.titlepad": 25})

#Considering PPO/Paraffin/LAB (appearance)
plt.plot(Enu,evt.dNdEvebar(Enu,0*ct.Ue4_2,0*ct.Umu4_2,ct.DelM2),'g',linewidth=1.5, label=r'$|U_{e4}|^{2}$=0, $|U_{\mu4}|^{2}$=0')
plt.plot(Enu,evt.dNdEvebar(Enu,ct.Ue4_2,ct.Umu4_2,ct.DelM2),'b',linewidth=1.5, label=r'$|U_{e4}|^{2}$=0.019, $|U_{\mu4}|^{2}$=0.015')
plt.plot(Enu,evt.dNdEvebar(Enu,3*ct.Ue4_2,3*ct.Umu4_2,ct.DelM2),'r',linewidth=1.5, label=r'$|U_{e4}|^{2}$=3*0.019, $|U_{\mu4}|^{2}$=3*0.015')
plt.title('\n'.join(wrap(r'Espectro dos antineutrinos do elétron para L={0}m IBD em PPO/Paraffin/LAB'.format(exp.Ljsns2),50)))
plt.legend()
plt.grid(True)
plt.xlabel(r"Energia dos neutrinos [MeV]")
plt.ylabel(r'dN/dE [MeV$^{-1}$]')
plt.show()


#Considering 208Pb (1ton) (charged current electron neutrino)

plt.plot(EnuPb,evt.dNdEvee(EnuPb,0,ct.DelM2),'b',linewidth=1.5, label=r'$|U_{e4}|^{2}$=0, $|U_{\mu4}|^{2}$=0')
plt.plot(EnuPb,evt.dNdEvee(EnuPb,ct.Ue4_2,ct.DelM2),'r',linewidth=1.5, label=r'$|U_{e4}|^{2}$=0.019, $|U_{\mu4}|^{2}$=0.015')
plt.plot(EnuPb,evt.dNdEvee(EnuPb,10*ct.Ue4_2,ct.DelM2),'g',linewidth=1.5, label=r'$|U_{e4}|^{2}$=10*0.019, $|U_{\mu4}|^{2}$=10*0.015')
plt.title('\n'.join(wrap(r'Espectro dos neutrinos do elétron para L={0}m corrente carregada em $^{{208}}$Pb'.format(exp.Ljsns2),50)))
plt.grid(True)
plt.legend(prop={'size': 15})
plt.xlabel(r"Energia dos neutrinos [MeV]")
plt.ylabel(r'dN/dE [MeV$^{-1}$]')
plt.show()


#Considering 208Pb (1ton) (neutral current electron neutrino)

plt.plot(EnuPb,evt.dNdEveve(EnuPb,ct.Ue4_2,ct.DelM2),'r',linewidth=1.5)
plt.title('\n'.join(wrap(r'Espectro dos neutrinos do elétron para L={0}m corrente neutra em $^{{208}}$Pb'.format(exp.Ljsns2),50)))
plt.grid(True)
plt.xlabel(r"Energia dos neutrinos [MeV]")
plt.ylabel(r'dN/dE [MeV$^{-1}$]')
plt.show()


#Considering 208Pb (1ton) (neutral current muon neutrino)

plt.plot(EnuPb,evt.dNdEvmvm(EnuPb,ct.Ue4_2,ct.Umu4_2,ct.DelM2),'r',linewidth=1.5)
plt.title('\n'.join(wrap(r'Espectro dos neutrinos do múon para L={0}m corrente neutra em $^{{208}}$Pb'.format(exp.Ljsns2),50)))
plt.ticklabel_format(axis='y', scilimits=(0,0))
plt.grid(True)
plt.xlabel(r"Energia dos neutrinos [MeV]")
plt.ylabel(r'dN/dE [MeV$^{-1}$]')
plt.show()


#Considering 208Pb (1ton) (neutral current tau neutrino)

plt.plot(EnuPb,evt.dNdEvevt(EnuPb,ct.Ue4_2,ct.Ut4_2,ct.DelM2),'r',linewidth=1.5)
plt.title('\n'.join(wrap(r'Espectro dos neutrinos do tau para L={0}m corrente neutra em $^{{208}}$Pb'.format(exp.Ljsns2),50)))
plt.ticklabel_format(axis='y', scilimits=(0,0))
plt.grid(True)
plt.xlabel(r"Energia dos neutrinos [MeV]")
plt.ylabel(r'dN/dE [MeV$^{-1}$]')
plt.show()


#Considering 208Pb (1ton) (neutral current electron antineutrino)

plt.plot(EnuPb,evt.dNdEvebarvebar(EnuPb,ct.Ue4_2,ct.Umu4_2,ct.DelM2),'r',linewidth=1.5)
plt.title('\n'.join(wrap(r'Espectro dos antineutrinos do elétron para L={0}m corrente neutra em $^{{208}}$Pb'.format(exp.Ljsns2),50)))
plt.ticklabel_format(axis='y', scilimits=(0,0))
plt.grid(True)
plt.xlabel(r"Energia dos antineutrinos [MeV]")
plt.ylabel(r'dN/dE [MeV$^{-1}$]')
plt.show()


#Considering 208Pb (1ton) (neutral current muon antineutrino)

plt.plot(EnuPb,evt.dNdEvmbarvmbar(EnuPb,ct.Umu4_2,ct.DelM2),'r',linewidth=1.5)
plt.title('\n'.join(wrap(r'Espectro dos antineutrinos do múon para L={0}m corrente neutra em $^{{208}}$Pb'.format(exp.Ljsns2),50)))
plt.grid(True)
plt.xlabel(r"Energia dos antineutrinos [MeV]")
plt.ylabel(r'dN/dE [MeV$^{-1}$]')
plt.show()


#Considering 208Pb (1ton) (neutral current tau antineutrino)

plt.plot(EnuPb,evt.dNdEvtbarvtbar(EnuPb,ct.Umu4_2,ct.Ut4_2,ct.DelM2),'r',linewidth=1.5)
plt.title('\n'.join(wrap(r'Espectro dos antineutrinos do tau para L={0}m corrente neutra em $^{{208}}$Pb'.format(exp.Ljsns2),50)))
plt.ticklabel_format(axis='y', scilimits=(0,0))
plt.grid(True)
plt.xlabel(r"Energia dos antineutrinos [MeV]")
plt.ylabel(r'dN/dE [MeV$^{-1}$]')
plt.show()