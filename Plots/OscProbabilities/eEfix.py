# This code plots the survival probability of electron neutrinos with fixed energy
# author: P. Chimenti, R.Bassi

from SterileDar import OscillationModel
import matplotlib.pyplot as plt
from SterileDar import constants as ct
import numpy as np

print("Gráfico da probabilidade de sobrevivência do neutrino do elétron para energia fixa")

model = OscillationModel.OscillationModel()


plt.rcParams.update({
    "figure.figsize": [8.0,6.0],
    "figure.dpi": 72.0,
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica"],
    "font.size": 16,
    "axes.titlepad": 25})

L = np.arange(0,2*ct.Ljsns2)
E = 35 #float(input("insira um valor para a energia ")) 

plt.plot(L,model.Pee(L,E,ct.Ue4_2,ct.DelM2),'r')
plt.title(r'Sobrevivência do neutrino do elétron para E={0}MeV'.format(E))
textstr = '\n'.join((
    r'$|U_{{e4}}|^{{2}}$= {0}'.format(ct.Ue4_2),
    r'$\Delta m^{{2}}$= {0}eV$^{{2}}$'.format(ct.DelM2)))
plt.text(-1,0.95,textstr, fontsize = 16, bbox = dict(facecolor = 'white', alpha = 1))
plt.grid(True)
plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.5)
plt.xlabel(r'Distância [m]')
plt.ylabel(r'Probabilidade de sobrevivência')
plt.tight_layout()
plt.savefig('NUesurvival{0}Mev.pdf'.format(E))
#plt.show()