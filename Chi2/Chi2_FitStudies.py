# Code to study the Chi2 function
from SterileDar import constants as ct
from SterileDar import expdata as exp
from SterileDar import Events
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2
import scipy.integrate as integrate
from numpy import  random as rn
import itertools as itt
from SterileDar import EventsnumberCC

evcc = EventsnumberCC.EventsnumberCC()
evt = Events.Events()
int_err = 0.01

# Energies for plotting
lead_min_e = 6
EnuPb = np.arange(lead_min_e,ct.muonmass/2,.2)                   # for Lead

#Considering 208Pb (1ton) (desappearance)
ntotalve_osc_bf = [evcc.ntotalve(ct.Ue4_2,ct.Umu4_2,ct.DelM2)]

print("Configuração: Ue4={0}, Umu4={1}, DelM2={2}".format(ct.Ue4_2,ct.Umu4_2,ct.DelM2))
print("Número total de interações de neutrinos do elétron em um ano:{0}".format(ntotalve_osc_bf))

ntotalve_noosc = [evcc.ntotalve(0,0,0)]
print("Configuração: Ue4={0}, Umu4={1} DelM2={2}".format(0,0,0))
print("Número total de interações de neutrinos do elétron em um ano:{0}".format(ntotalve_noosc))

bins = np.arange(lead_min_e, ct.muonmass/2 + 0.01, (ct.muonmass/2 - lead_min_e)/10 )
measured     = np.zeros(len(bins) - 1)
prediction   = np.zeros(len(bins) - 1)

for i in range(len(bins) - 1):
    if i == 6:
        measured[i] = rn.poisson([integrate.quad(lambda Enu1: evt.dNdEvee(Enu1,ct.Ue4_2,ct.DelM2), bins[i], bins[i+1], epsabs=int_err)][0][0] + evt.NMuOriginCC(ct.NuMuenergy,ct.Ue4_2,ct.Umu4_2,ct.DelM2))
    else:
        measured[i] = rn.poisson([integrate.quad(lambda Enu1: evt.dNdEvee(Enu1,ct.Ue4_2,ct.DelM2), bins[i], bins[i+1], epsabs=int_err)][0][0])
  

def chi2_someconfig(Ue4, Umu4, DelM2):
    """ Esta função bla bla bla
    """
    chi2_val = 0.
    for i in range(len(bins) - 1 ):
        if i == 6:
            prediction[i] = [integrate.quad(lambda Enu1: evt.dNdEvee(Enu1,Ue4,DelM2), bins[i], bins[i+1], epsabs=int_err)][0][0] + evt.NMuOriginCC(ct.NuMuenergy,Ue4,Umu4,DelM2)
        else:
            prediction[i] = [integrate.quad(lambda Enu1: evt.dNdEvee(Enu1,Ue4,DelM2), bins[i], bins[i+1], epsabs=int_err)][0][0]
        chi2_val+= ((measured[i]-prediction[i])**2)/prediction[i]
    return chi2_val

v_chi2 = np.vectorize(chi2_someconfig)

x_ue4 = np.linspace(0,0.04,100)
plt.plot(x_ue4, v_chi2(x_ue4,ct.Umu4_2,ct.DelM2))
plt.show()
