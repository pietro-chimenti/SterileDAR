# This code plots the Inverse beta decay cross section at first order arxiv:9903554 equation (14)
# author: P. Chimenti, R.Bassi

from SterileDar import constants as ct
from SterileDar import crosssections
import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt
import matplotlib.font_manager

cs=crosssections.crosssections()

int_err = 0.01
Enu     = np.arange(ct.energythresholdIBD , ct.muonmass/2, 0.5)

result = [integrate.quad(lambda costheta: cs.dsigmadcos(costheta,Enu), -1, 1, epsabs=int_err)
          for Enu in np.arange(ct.energythresholdIBD, ct.muonmass/2, .5)]

plot = []
for i in result:
    plot.append(i[0])

plt.show()


plt.rcParams.update({
    "figure.figsize": [8.0,6.0],
    "figure.dpi": 72.0,
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.size": 16,
    "font.sans-serif": ["Helvetica"]})
plt.title(u'Seção de choque IBD a primeira ordem')
plt.plot(Enu, plot, 'r')
plt.grid(True)
plt.xlabel(r"Energia dos neutrinos [MeV]")
plt.ylabel(r"Seção de choque [m$^{2}$]")
plt.tight_layout()
plt.savefig('CS_IBD_1_order.pdf')
#plt.show()