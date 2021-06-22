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

result = [integrate.quad(lambda theta: cs.dsigmadcos(theta,Enu), 0, 2*np.pi, epsabs=int_err)
          for Enu in np.arange(ct.energythresholdIBD, ct.muonmass/2, .5)]

plot = []
for i in result:
    plot.append(i[0])

plt.show()


plt.rcParams.update({
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica"]})
plt.title(u'Seção de choque IBD a primeira ordem')
plt.plot(Enu, plot, 'r')
plt.grid(True)
plt.xlabel(r"Energia dos neutrinos [MeV]")
plt.ylabel(r"Seção de choque [m$^{2}$]")
plt.show()