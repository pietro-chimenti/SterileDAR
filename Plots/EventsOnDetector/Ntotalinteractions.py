# This code prints the calculated number of interactions of both neutrinos and antineutrinos
# and a table with the information for neutral and charged current
# author: P. Chimenti, R.Bassi

from SterileDar import EventsnumberCC
from SterileDar import EventsnumberNC
import matplotlib.pyplot as plt
from SterileDar import constants as ct
import numpy as np


cc = EventsnumberCC.EventsnumberCC()
nc = EventsnumberNC.EventsnumberNC()


#Considering PPO/Paraffin/LAB (appearance)

print("Número total de interações de antineutrinos do elétron em um ano (PPO/Paraffin/LAB):{0}  ".format(cc.ntotalvebar(ct.Ue4_2,ct.Umu4_2,ct.DelM2)))


#Considering 208Pb (1ton) (desappearance) (charged current)

print("Número total de interações de neutrinos do elétron em um ano por corrente carregada:{0}".format(cc.ntotalve(ct.Ue4_2,ct.Umu4_2,ct.DelM2)))


#Considering 208Pb (1ton) (neutral current electron neutrino)

print("Número total de interações de neutrinos do elétron em um ano por corrente neutra:{0}".format(nc.ntotalveve(ct.Ue4_2,ct.Umu4_2,ct.DelM2)))


#Considering 208Pb (1ton) (neutral current muon neutrino)

print("Número total de interações de neutrinos do múon em um ano por corrente neutra:{0}".format(nc.ntotalvmvm(ct.Ue4_2,ct.Umu4_2,ct.DelM2)))


#Considering 208Pb (1ton) (neutral current tau neutrino)

print("Número total de interações de neutrinos do tau em um ano por corrente neutra:{0}".format(nc.ntotalvtvt(ct.Ue4_2,ct.Umu4_2,ct.Ut4_2,ct.DelM2)))


#Considering 208Pb (1ton) (neutral current electron antineutrino)

print("Número total de interações de antineutrinos do elétron em um ano por corrente neutra:{0}".format(nc.ntotalvebarvebar(ct.Ue4_2,ct.Umu4_2,ct.DelM2)))


#Considering 208Pb (1ton) (neutral current muon antineutrino)

print("Número total de interações de antineutrinos do muon em um ano por corrente neutra:{0}".format(nc.ntotalvmbarvmbar(ct.Umu4_2,ct.DelM2)))


#Considering 208Pb (1ton) (neutral current tau antineutrino)

print("Número total de interações de antineutrinos do tau em um ano por corrente neutra:{0}".format(nc.ntotalvtbarvtbar(ct.Umu4_2,ct.Ut4_2,ct.DelM2)))


#=Table with information

fig = plt.figure(dpi=125)
ax = fig.add_subplot(1,1,1)
table_data=[
    [r"$\nu_{e}^{(CC)}$", "{0}".format(np.round(cc.ntotalve(ct.Ue4_2,ct.Umu4_2,ct.DelM2), 2))],
    [r"$\nu_{e}^{(NC)}$", "{0}".format(np.round(nc.ntotalveve(ct.Ue4_2,ct.Umu4_2,ct.DelM2),2))],
    [r"$\nu_{\mu}^{(NC)}$", "{0}".format(np.round(nc.ntotalvmvm(ct.Ue4_2,ct.Umu4_2,ct.DelM2),2))],
    [r"$\nu_{\tau}^{(NC)}$", "{0}".format(np.round(nc.ntotalvtvt(ct.Ue4_2,ct.Umu4_2,ct.Ut4_2,ct.DelM2),2))],
    [r"$\bar{\nu}_{e}^{(NC)}$", "{0}".format(np.round(nc.ntotalvebarvebar(ct.Ue4_2,ct.Umu4_2,ct.DelM2),2))],
    [r"$\bar{\nu}_{\mu}^{(NC)}$", "{0}".format(np.round(nc.ntotalvmbarvmbar(ct.Umu4_2,ct.DelM2),2))],
    [r"$\bar{\nu}_{\tau}^{(NC)}$", "{0}".format(np.round(nc.ntotalvtbarvtbar(ct.Umu4_2,ct.Ut4_2,ct.DelM2),2))],
     [r"Total", "{0}".format(np.round((cc.ntotalve(ct.Ue4_2,ct.Umu4_2,ct.DelM2) + nc.ntotalveve(ct.Ue4_2,ct.Umu4_2,ct.DelM2) 
                                       + nc.ntotalvmvm(ct.Ue4_2,ct.Umu4_2,ct.DelM2) + nc.ntotalvtvt(ct.Ue4_2,ct.Umu4_2,ct.Ut4_2,ct.DelM2) 
                                       + nc.ntotalvebarvebar(ct.Ue4_2,ct.Umu4_2,ct.DelM2) + nc.ntotalvmbarvmbar(ct.Umu4_2,ct.DelM2) 
                                       + nc.ntotalvtbarvtbar(ct.Umu4_2,ct.Ut4_2,ct.DelM2)),2))]
    
]

table_label = ["Tipo de Neutrino", "Número de interações"]

ccolors = plt.cm.BuPu(np.full(len(table_label), 0.15))

table = ax.table(cellText=table_data, cellLoc='center', loc='center', colColours=ccolors, colLabels=table_label, edges='closed')
table.set_fontsize(14)
table.scale(1,2)
ax.axis('off')

plt.title('Número de interações durante um ano')
plt.show()