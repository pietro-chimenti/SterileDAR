# This code plots the survival probability of muon neutrinos with fixed energy
# author: P. Chimenti, R.Bassi

from SterileDar import OscillationModel
import matplotlib.pyplot as plt
from SterileDar import constants as ct
import numpy as np

print("Gráfico da probabilidade de sobrevivência do neutrino do múon para energia fixa")

model = OscillationModel.OscillationModel()


plt.rcParams.update({
    "figure.figsize": [8.0,6.0],
    "figure.dpi": 72.0,
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica"],
    "font.size": 16,
    "axes.titlepad": 25})

L = np.arange(0,2*ct.Ljsns2,0.01)
E = 30 #float(input('Digite um valor fixo para a energia: '))

plt.plot(L,model.Pmm(L,E,ct.Umu4_2,ct.DelM2),'r')
plt.title(r'Sobrevivência do neutrino do múon para E={0}MeV'.format(E))
plt.grid(True)
textstr = '\n'.join((
    r'$|U_{{\mu 4}}|^{{2}}$= {0}'.format(ct.Umu4_2),
    r'$\Delta m^{{2}}$= {0}eV$^{{2}}$'.format(ct.DelM2)))
plt.text(-1,0.96,textstr, fontsize = 16, bbox = dict(facecolor = 'white', alpha = 1))
plt.xlabel(r'Distância [m]')
plt.ylabel(r'Probabilidade de sobrevivência')
plt.tight_layout()
plt.savefig('NUmusurvival{0}Mev.pdf'.format(E))
#plt.show()