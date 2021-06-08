import sys
sys.path.append("..")
from SterileDar import EventsnumberCC
from SterileDar import EventsnumberNC
import matplotlib.pyplot as plt
from SterileDar import constants as ct
import numpy as np

evcc = EventsnumberCC.EventsnumberCC()
evnc = EventsnumberNC.EventsnumberNC()
DelM2 = np.arange(0,20,.2)


#Considering 208Pb (1ton) (desappearance) (charged current)

Numberve = [evcc.ntotalve(ct.Ue4_2,ct.Umu4_2,DelM2)
          for DelM2 in DelM2]

plt.plot(DelM2,Numberve,'r',linewidth=1.0)
plt.title(r'Número de Interações de $\nu_{e}^{(CC)}$ em função de $\Delta m^{2}$')
plt.grid(True)
plt.xlabel(r"$\Delta m^{2}$ [MeV]")
plt.ylabel(r'Número de Interações')
plt.show()


#Considering 208Pb (1ton) (neutral current electron neutrino)
    
Numberveve = [evnc.ntotalveve(ct.Ue4_2,ct.Umu4_2,DelM2)
          for DelM2 in DelM2]

plt.plot(DelM2,Numberveve,'r',linewidth=1.0)
plt.title(r'Número de Interações de $\nu_{e}^{(NC)}$ em função de $\Delta m^{2}$')
plt.grid(True)
plt.xlabel(r"$\Delta m^{2}$ [MeV]")
plt.ylabel(r'Número de Interações')
plt.show()


#Considering 208Pb (1ton) (neutral current muon neutrino)

Numbervmvm = [evnc.ntotalvmvm(ct.Ue4_2,ct.Umu4_2,DelM2)
          for DelM2 in DelM2]

plt.plot(DelM2,Numbervmvm,'r',linewidth=1.0)
plt.title(r'Número de Interações de $\nu_{\mu}^{(NC)}$ em função de $\Delta m^{2}$')
plt.grid(True)
plt.xlabel(r"$\Delta m^{2}$ [MeV]")
plt.ylabel(r'Número de Interações')
plt.show()


#Considering 208Pb (1ton) (neutral current tau neutrino)

Numbervtvt = [evnc.ntotalvtvt(ct.Ue4_2,ct.Umu4_2,ct.Ut4_2,DelM2)
          for DelM2 in DelM2]

plt.plot(DelM2,Numbervtvt,'r',linewidth=1.0)
plt.title(r'Número de Interações de $\nu_{\tau}^{(NC)}$ em função de $\Delta m^{2}$')
plt.grid(True)
plt.xlabel(r"$\Delta m^{2}$ [MeV]")
plt.ylabel(r'Número de Interações')
plt.show() 


#Considering 208Pb (1ton) (neutral current electron antineutrino)

Numbervebarvebar = [evnc.ntotalvebarvebar(ct.Ue4_2,ct.Umu4_2,DelM2)
          for DelM2 in DelM2]

plt.plot(DelM2,Numbervebarvebar,'r',linewidth=1.0)
plt.title(r'Número de Interações de $\bar{\nu}_{e}^{(NC)}$ em função de $\Delta m^{2}$')
plt.grid(True)
plt.xlabel(r"$\Delta m^{2}$ [MeV]")
plt.ylabel(r'Número de Interações')
plt.show()


#Considering 208Pb (1ton) (neutral current muon antineutrino)

Numbervmbarvmbar = [evnc.ntotalvmbarvmbar(ct.Umu4_2,DelM2)
          for DelM2 in DelM2]

plt.plot(DelM2,Numbervmbarvmbar,'r',linewidth=1.0)
plt.title(r'Número de Interações de $\bar{\nu}_{\mu}^{(NC)}$ em função de $\Delta m^{2}$')
plt.grid(True)
plt.xlabel(r"$\Delta m^{2}$ [MeV]")
plt.ylabel(r'Número de Interações')
plt.show()


#Considering 208Pb (1ton) (neutral current tau antineutrino)

Numbervtbarvtbar = [evnc.ntotalvtbarvtbar(ct.Umu4_2,ct.Ut4_2,DelM2)
          for DelM2 in DelM2]

plt.plot(DelM2,Numbervtbarvtbar,'r',linewidth=1.0)
plt.title(r'Número de Interações de $\bar{\nu}_{\tau}^{(NC)}$ em função de $\Delta m^{2}$')
plt.grid(True)
plt.xlabel(r"$\Delta m^{2}$ [MeV]")
plt.ylabel(r'Número de Interações')
plt.show()

#Total

zipped_lists = zip(Numberve, Numberveve, Numbervmvm, Numbervtvt, Numbervebarvebar, Numbervmbarvmbar, Numbervtbarvtbar)

sum = [x1 + x2 + x3 + x4 + x5 + x6 + x7 for (x1, x2, x3, x4, x5, x6, x7) in zipped_lists]

plt.plot(DelM2,sum,'r',linewidth=1.0)
plt.title(r'Número total de Interações de $\nu$ em função de $\Delta m^{2}$')
plt.grid(True)
plt.xlabel(r"$\Delta m^{2}$ [MeV]")
plt.ylabel(r'Número de Interações')
plt.show()