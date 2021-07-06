# This code plots the survival probability of muon neutrinos with a fixed distance
# author: P. Chimenti, R.Bassi

from SterileDar import OscillationModel
import matplotlib.pyplot as plt
from SterileDar import constants as ct
import numpy as np

print("Gráfico da probabilidade de sobrevivência do neutrino do múon para distância fixa")

model = OscillationModel.OscillationModel()


plt.rcParams.update({
    "figure.figsize": [8.0,6.0],
    "figure.dpi": 72.0,
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica"],
    "font.size": 16,
    "axes.titlepad": 25})

E = np.arange(4,ct.muonmass/2,0.01)
L = ct.Ljsns2 #float(input('Digite um valor fixo para a distância: '))

plt.plot(E,model.Pmm(L,E,ct.Umu4_2,ct.DelM2),'r')
plt.title('Sobrevivência do neutrino do múon para L={0}m'.format(L))
plt.grid(True)
textstr = '\n'.join((
    r'$|U_{{\mu 4}}|^{{2}}$= {0}'.format(ct.Umu4_2),
    r'$\Delta m^{{2}}$= {0}eV$^{{2}}$'.format(ct.DelM2)))
plt.text(40,0.99,textstr, fontsize = 16, bbox = dict(facecolor = 'white', alpha = 1))
plt.xlabel('Energia [MeV]')
plt.ylabel('Probabilidade de sobrevivência')
plt.tight_layout()
plt.savefig('NUmusurvival{0}m.pdf'.format(L))
#plt.show()