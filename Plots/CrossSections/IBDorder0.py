# This code plots the IBD cross section at zeroth order arxiv:9903554 equation (10)
# author: P. Chimenti, R.Bassi

from SterileDar import constants as ct
from SterileDar import crosssections
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager

cs=crosssections.crosssections()

Enu= np.arange(ct.energythresholdIBD,ct.muonmass/2,.5)


plt.rcParams.update({
    "figure.figsize": [8.0,6.0],
    "figure.dpi": 72.0,
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.size": 16,
    "font.sans-serif": ["Helvetica"]})
plt.title(u'Seção de choque IBD a ordem zero')
plt.plot(Enu,cs.sigmaIBD(Enu),'r')
plt.grid(True)
plt.xlabel(r"Energia dos neutrinos [MeV]")
plt.ylabel(r"Seção de choque [m$^{2}$]")
plt.tight_layout()
plt.savefig('CS_IBD_0_order.pdf')
#plt.show()