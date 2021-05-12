# Chi2 to test electron neutrino disappearence 
# author: P. Chimenti, R.Bassi
# date:   26/11/2020

#import sys
#sys.path.append("..")
from SterileDar import constants as ct
from SterileDar import expdata as exp
from SterileDar import Events
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
from numpy import  random as rn
import itertools as itt

evt = Events.Events()
int_err = 0.01

# Energies for plotting
lead_min_e = 6
Enu = np.arange(ct.energythresholdIBD,ct.muonmass/2,.2) # for IBD
EnuPb = np.arange(lead_min_e,ct.muonmass/2,.2)                   # for Lead

#Considering 208Pb (1ton) (desappearance)
ntotalve_osc_bf = [integrate.quad(lambda Enu1: evt.dNdEvee(Enu1,ct.Ue4_2,ct.DelM2), lead_min_e, ct.muonmass/2, epsabs=int_err)]

print("Configuração: Ue4={0}, DelM2={1}".format(ct.Ue4_2,ct.DelM2))
print("Número total de interações de neutrinos do elétron em um ano:{0}".format(ntotalve_osc_bf))

ntotalve_noosc = [integrate.quad(lambda Enu1: evt.dNdEvee(Enu1,0,0), lead_min_e, ct.muonmass/2, epsabs=int_err)]
print("Configuração: Ue4={0}, DelM2={1}".format(0,0))
print("Número total de interações de neutrinos do elétron em um ano:{0}".format(ntotalve_noosc))

bins = np.arange(lead_min_e, ct.muonmass/2 + 0.01, (ct.muonmass/2 - lead_min_e)/10 )
measured = np.zeros(len(bins) - 1)
no_osc   = np.zeros(len(bins) - 1)

for i in range(len(bins) -1 ):
    no_osc[i] = [integrate.quad(lambda Enu1: evt.dNdEvee(Enu1,0,0), bins[i], bins[i+1], epsabs=int_err)][0][0]

def chi2_someconfig(Ue4, DelM2):
    """ Esta função bla bla bla
    """
    rn.seed(20210511)
    for i in itt.count():
        chi2 = 0.
        for i in range(len(bins) -1 ):
            measured[i] = rn.poisson([integrate.quad(lambda Enu1: evt.dNdEvee(Enu1,Ue4,DelM2), bins[i], bins[i+1], epsabs=int_err)][0][0])
            chi2+= ((measured[i]-no_osc[i])**2)/no_osc[i]
        yield chi2

chi2_gen = chi2_someconfig(0.,1.0)

chi2_values = [ next(chi2_gen) for i in range(1000)  ]

plt.hist(chi2_values, bins = 100)
plt.show()