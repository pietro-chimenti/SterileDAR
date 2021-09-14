# This code plots the IBD cross section at zeroth order arxiv:9903554 equation (10)
# author: P. Chimenti, R.Bassi

from SterileDar import constants as ct
from SterileDar import crosssections
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager
import scipy.integrate as integrate

cs=crosssections.crosssections()

Enu= np.arange(ct.energythresholdIBD,ct.muonmass/2,.5)

int_err = 0.01


result = [integrate.quad(lambda costheta: cs.dsigmadcos(costheta,Enu), -1, 1, epsabs=int_err)
          for Enu in np.arange(ct.energythresholdIBD, ct.muonmass/2, .5)]

plot = []
for i in result:
    plot.append(i[0])


plt.rcParams.update({
    "figure.figsize": [8.0,6.0],
    "figure.dpi": 72.0,
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.size": 16,
    "font.sans-serif": ["Helvetica"]})
plt.title(u'Seção de choque IBD')
plt.plot(Enu,cs.sigmaIBD(Enu),'r',label='Ordem Zero')
plt.plot(Enu, plot, 'b',label='Primeira Ordem')
plt.grid(True)
plt.xlabel(r"Energia dos neutrinos [MeV]")
plt.ylabel(r"Seção de choque [m$^{2}$]")
plt.tight_layout()
plt.legend(prop={'size': 15}, loc='upper left')
plt.savefig('CS_IBD_01.pdf')
#plt.show()