#table with total information about interactions
import sys
sys.path.append("..")
from SterileDar import EventsnumberCC as cc
from SterileDar import EventsnumberNC as nc
import matplotlib.pyplot as plt
from SterileDar import constants as ct
from SterileDar import expdata as exp
from SterileDar import Events
import numpy as np

evt = Events.Events()
Enu = np.arange(ct.energythresholdIBD,ct.muonmass/2,.2)
EnuPb = np.arange(5,ct.muonmass/2,.2)


#Considering PPO/Paraffin/LAB (appearance)
plt.plot(Enu,evt.dNdEvebar(Enu,ct.Ue4_2,ct.Umu4_2,ct.DelM2),'r',linewidth=1.0)
plt.plot(Enu,evt.dNdEvebar(Enu,0.025,0.025,ct.DelM2),'b',linewidth=1.0)
plt.title(r'Espectro dos antineutrinos do elétron para L={0}m'.format(exp.Ljsns2))
plt.grid(True)
plt.xlabel(r"Energia dos neutrinos [MeV]")
plt.ylabel(r'dN/dE [MeV$^{-1}$]')
plt.show()

print("Número total de interações de antineutrinos do elétron em um ano:{0}".format(cc.ntotalvebar))

#Considering 208Pb (1ton) (desappearance) (charged current)

plt.plot(EnuPb,evt.dNdEvee(EnuPb,ct.Ue4_2,ct.DelM2),'r',linewidth=1.0)
plt.plot(EnuPb,evt.dNdEvee(EnuPb,0,ct.DelM2),'b',linewidth=1.0)
plt.plot(EnuPb,evt.dNdEvee(EnuPb,10*ct.Ue4_2,ct.DelM2),'g',linewidth=1.0)
plt.title(r'Espectro dos neutrinos do elétron para L={0}m'.format(exp.Ljsns2))
plt.grid(True)
plt.xlabel(r"Energia dos neutrinos [MeV]")
plt.ylabel(r'dN/dE [MeV$^{-1}$]')
plt.show()

print("Número total de interações de neutrinos do elétron em um ano por corrente carregada:{0}".format(cc.ntotalve))

#Considering 208Pb (1ton) (neutral current electron neutrino)

plt.plot(EnuPb,evt.dNdEveve(EnuPb,ct.Ue4_2,ct.DelM2),'r',linewidth=1.0)
plt.title(r'Espectro dos neutrinos do elétron para L={0}m'.format(exp.Ljsns2))
plt.grid(True)
plt.xlabel(r"Energia dos neutrinos [MeV]")
plt.ylabel(r'dN/dE [MeV$^{-1}$]')
plt.show()

print("Número total de interações de neutrinos do elétron em um ano por corrente neutra:{0}".format(nc.ntotalveve))

#Considering 208Pb (1ton) (neutral current muon neutrino)

plt.plot(EnuPb,evt.dNdEvmvm(EnuPb,ct.Ue4_2,ct.Umu4_2,ct.DelM2),'r',linewidth=1.0)
plt.title(r'Espectro dos neutrinos do múon para L={0}m'.format(exp.Ljsns2))
plt.grid(True)
plt.xlabel(r"Energia dos neutrinos [MeV]")
plt.ylabel(r'dN/dE [MeV$^{-1}$]')
plt.show()

print("Número total de interações de neutrinos do múon em um ano por corrente neutra:{0}".format(nc.ntotalvmvm))

#Considering 208Pb (1ton) (neutral current tau neutrino)

plt.plot(EnuPb,evt.dNdEvevt(EnuPb,ct.Ue4_2,ct.Ut4_2,ct.DelM2),'r',linewidth=1.0)
plt.title(r'Espectro dos neutrinos do tau para L={0}m'.format(exp.Ljsns2))
plt.grid(True)
plt.xlabel(r"Energia dos neutrinos [MeV]")
plt.ylabel(r'dN/dE [MeV$^{-1}$]')
plt.show()

print("Número total de interações de neutrinos do tau em um ano por corrente neutra:{0}".format(nc.ntotalvtvt))

#Considering 208Pb (1ton) (neutral current electron antineutrino)

plt.plot(EnuPb,evt.dNdEvebarvebar(EnuPb,ct.Ue4_2,ct.Umu4_2,ct.DelM2),'b',linewidth=1.0)
plt.title(r'Espectro dos antineutrinos do elétron para L={0}m'.format(exp.Ljsns2))
plt.grid(True)
plt.xlabel(r"Energia dos antineutrinos [MeV]")
plt.ylabel(r'dN/dE [MeV$^{-1}$]')
plt.show()

print("Número total de interações de antineutrinos do elétron em um ano por corrente neutra:{0}".format(nc.ntotalvebarvebar))

#Considering 208Pb (1ton) (neutral current muon antineutrino)

plt.plot(EnuPb,evt.dNdEvmbarvmbar(EnuPb,ct.Umu4_2,ct.DelM2),'b',linewidth=1.0)
plt.title(r'Espectro dos antineutrinos do muon para L={0}m'.format(exp.Ljsns2))
plt.grid(True)
plt.xlabel(r"Energia dos antineutrinos [MeV]")
plt.ylabel(r'dN/dE [MeV$^{-1}$]')
plt.show()

print("Número total de interações de antineutrinos do muon em um ano por corrente neutra:{0}".format(nc.ntotalvmbarvmbar))

#Considering 208Pb (1ton) (neutral current tau antineutrino)

plt.plot(EnuPb,evt.dNdEvtbarvtbar(EnuPb,ct.Umu4_2,ct.Ut4_2,ct.DelM2),'b',linewidth=1.0)
plt.title(r'Espectro dos antineutrinos do tau para L={0}m'.format(exp.Ljsns2))
plt.grid(True)
plt.xlabel(r"Energia dos antineutrinos [MeV]")
plt.ylabel(r'dN/dE [MeV$^{-1}$]')
plt.show()

print("Número total de interações de antineutrinos do tau em um ano por corrente neutra:{0}".format(nc.ntotalvtbarvtbar))

#table with information

fig = plt.figure(dpi=125)
ax = fig.add_subplot(1,1,1)
table_data=[
    [r"$\nu_{e}^{(CC)}$", "{0}".format(cc.ntotalve)],
    [r"$\nu_{e}^{(NC)}$", "{0}".format(nc.ntotalveve)],
    [r"$\nu_{\mu}^{(NC)}$", "{0}".format(nc.ntotalvmvm)],
    [r"$\nu_{\tau}^{(NC)}$", "{0}".format(nc.ntotalvtvt)],
    [r"$\bar{\nu}_{e}^{(NC)}$", "{0}".format(nc.ntotalvebarvebar)],
    [r"$\bar{\nu}_{\mu}^{(NC)}$", "{0}".format(nc.ntotalvmbarvmbar)],
    [r"$\bar{\nu}_{\tau}^{(NC)}$", "{0}".format(nc.ntotalvtbarvtbar)]
]

table_label = ["Tipo de Neutrino", "Número de interações"]

ccolors = plt.cm.BuPu(np.full(len(table_label), 0.15))

table = ax.table(cellText=table_data, cellLoc='center', loc='center', colColours=ccolors, colLabels=table_label, edges='closed')
table.set_fontsize(14)
table.scale(1,2)
ax.axis('off')

plt.title('Número de interações durante um ano')
plt.show()