# This code plots the number of interactions of each neutrino flavor and total as a function of Ue4^2
# author: P. Chimenti, R.Bassi

from SterileDar import EventsnumberCC
from SterileDar import EventsnumberNC
import matplotlib.pyplot as plt
from SterileDar import constants as ct
import numpy as np

evcc = EventsnumberCC.EventsnumberCC()
evnc = EventsnumberNC.EventsnumberNC()
Ue4_2 = np.arange(0.005,0.05,.0005)

plt.rcParams.update({
    "figure.figsize": [8.0,6.0],
    "figure.dpi": 72.0,
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica"],
    "font.size": 16,
    "axes.titlepad": 25})

#Considering 208Pb (1ton) (desappearance) (charged current)

Numberve = [evcc.ntotalve(Ue4_2,ct.Umu4_2,ct.DelM2)
          for Ue4_2 in Ue4_2]

plt.plot(Ue4_2,Numberve,'r',linewidth=1.5)
plt.title(r'Número de Interações de $\nu_{e}^{(CC)}$ em função de $|U_{e4}|^{2}$')
plt.grid(True)
textstr = '\n'.join((
    r'$|U_{{\mu 4}}|^{{2}}$= {0}'.format(ct.Umu4_2),
    r'$\Delta m^{{2}}$= {0}eV$^{{2}}$'.format(ct.DelM2),))
plt.text(0.005,1950,textstr, fontsize = 16, bbox = dict(facecolor = 'white', alpha = 1))
plt.xlabel(r"$|U_{e4}|^{2}$")
plt.ylabel(r'Número de Interações')
plt.savefig('NueCCUe4.pdf')
plt.close()


#Considering 208Pb (1ton) (neutral current electron neutrino)
    
Numberveve = [evnc.ntotalveve(Ue4_2,ct.Umu4_2,ct.DelM2)
          for Ue4_2 in Ue4_2]

plt.plot(Ue4_2,Numberveve,'r',linewidth=1.5)
plt.title(r'Número de Interações de $\nu_{e}^{(NC)}$ em função de $|U_{e4}|^{2}$')
plt.grid(True)
textstr = '\n'.join((
    r'$|U_{{\mu 4}}|^{{2}}$= {0}'.format(ct.Umu4_2),
    r'$\Delta m^{{2}}$= {0}eV$^{{2}}$'.format(ct.DelM2),))
plt.text(0.005,102,textstr, fontsize = 16, bbox = dict(facecolor = 'white', alpha = 1))
plt.xlabel(r"$|U_{e4}|^{2}$")
plt.ylabel(r'Número de Interações')
plt.savefig('NueNCUe4.pdf')
plt.close()


#Considering 208Pb (1ton) (neutral current muon neutrino)

Numbervmvm = [evnc.ntotalvmvm(Ue4_2,ct.Umu4_2,ct.DelM2)
          for Ue4_2 in Ue4_2]

plt.plot(Ue4_2,Numbervmvm,'r',linewidth=1.5)
plt.title(r'Número de Interações de $\nu_{\mu}^{(NC)}$ em função de $|U_{e4}|^{2}$')
plt.grid(True)
textstr = '\n'.join((
    r'$|U_{{\mu 4}}|^{{2}}$= {0}'.format(ct.Umu4_2),
    r'$\Delta m^{{2}}$= {0}eV$^{{2}}$'.format(ct.DelM2),))
plt.text(0.005,60.15,textstr, fontsize = 16, bbox = dict(facecolor = 'white', alpha = 1))
plt.xlabel(r"$|U_{e4}|^{2}$")
plt.ylabel(r'Número de Interações')
plt.savefig('NumuNCUe4.pdf')
plt.close()


#Considering 208Pb (1ton) (neutral current tau neutrino)

Numbervtvt = [evnc.ntotalvtvt(Ue4_2,ct.Umu4_2,ct.Ut4_2,ct.DelM2)
          for Ue4_2 in Ue4_2]

plt.plot(Ue4_2,Numbervtvt,'r',linewidth=1.5)
plt.title(r'Número de Interações de $\nu_{\tau}^{(NC)}$ em função de $|U_{e4}|^{2}$')
plt.grid(True)
textstr = '\n'.join((
    r'$|U_{{\mu 4}}|^{{2}}$= {0}'.format(ct.Umu4_2),
    r'$|U_{{\tau 4}}|^{{2}}$= {0}'.format(ct.Ut4_2),
    r'$\Delta m^{{2}}$= {0}eV$^{{2}}$'.format(ct.DelM2),))
plt.text(0.005,0.2,textstr, fontsize = 16, bbox = dict(facecolor = 'white', alpha = 1))
plt.xlabel(r"$|U_{e4}|^{2}$")
plt.ylabel(r'Número de Interações')
plt.savefig('NutauNCUe4.pdf')
plt.close() 


#Considering 208Pb (1ton) (neutral current electron antineutrino)

Numbervebarvebar = [evnc.ntotalvebarvebar(Ue4_2,ct.Umu4_2,ct.DelM2)
          for Ue4_2 in Ue4_2]

plt.plot(Ue4_2,Numbervebarvebar,'r',linewidth=1.5)
plt.title(r'Número de Interações de $\bar{\nu}_{e}^{(NC)}$ em função de $|U_{e4}|^{2}$')
plt.grid(True)
textstr = '\n'.join((
    r'$|U_{{\mu 4}}|^{{2}}$= {0}'.format(ct.Umu4_2),
    r'$\Delta m^{{2}}$= {0}eV$^{{2}}$'.format(ct.DelM2),))
plt.text(0.005,0.3,textstr, fontsize = 16, bbox = dict(facecolor = 'white', alpha = 1))
plt.xlabel(r"$|U_{e4}|^{2}$")
plt.ylabel(r'Número de Interações')
plt.savefig('NuebarNCUe4.pdf')
plt.close()


#Total

zipped_lists = zip(Numberve, Numberveve, Numbervmvm, Numbervtvt, Numbervebarvebar)

sum = [x1 + x2 + x3 + x4 + x5 for (x1, x2, x3, x4, x5) in zipped_lists]

plt.plot(Ue4_2,sum,'r',linewidth=1.5)
plt.title(r'Número total de Interações de $\nu$ em função de $|U_{e4}|^{2}$')
plt.grid(True)
textstr = '\n'.join((
    r'$|U_{{\mu 4}}|^{{2}}$= {0}'.format(ct.Umu4_2),
    r'$|U_{{\tau 4}}|^{{2}}$= {0}'.format(ct.Ut4_2),
    r'$\Delta m^{{2}}$= {0}eV$^{{2}}$'.format(ct.DelM2),))
plt.text(0.005,2050,textstr, fontsize = 16, bbox = dict(facecolor = 'white', alpha = 1))
plt.xlabel(r"$|U_{e4}|^{2}$")
plt.ylabel(r'Número de Interações')
plt.savefig('NutotalUe4.pdf')
plt.close()