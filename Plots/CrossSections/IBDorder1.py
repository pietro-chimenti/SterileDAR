# This code plots the Inverse beta decay cross section at first order arxiv:9903554 equation (14)
# author: P. Chimenti, R.Bassi

from SterileDar import constants as ct
from SterileDar import crosssections
import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt
import matplotlib.font_manager
from scipy.interpolate import interp1d

cs=crosssections.crosssections()
csibd1=crosssections.IBDfirstorder()


Enu = np.arange(ct.energythresholdIBD , ct.muonmass/2, 0.05)

plt.rcParams.update({
    "figure.figsize": [8.0,6.0],
    "figure.dpi": 72.0,
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.size": 16,
    "font.sans-serif": ["Helvetica"]})
plt.title(u'Seção de choque IBD a primeira ordem')
#plt.plot(Enu, plot, 'r')
plt.plot(Enu, csibd1.sigmaIBDorder1(Enu), 'b')
plt.grid(True)
plt.xlabel(r"Energia dos neutrinos [MeV]")
plt.ylabel(r"Seção de choque [m$^{2}$]")
plt.tight_layout()
#plt.savefig('CS_IBD_1_order.pdf')
plt.show()

######################################### NTOTAL IBD FIRST ORDER CALCULATION ###########################################

from SterileDar import expdata as exp
from SterileDar import Oscspec

osc = Oscspec.Oscspec()

nproton = float(exp.hidrogeniototal) #number of protons at the detector






    
print(ntotalvebaribd1(ct.Ue4_2,ct.Umu4_2,ct.DelM2))
