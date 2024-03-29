# Code to study the Chi2 function

# author: P. Chimenti, R.Bassi

from SterileDar import constants as ct
from SterileDar import InteractionSpectrum
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import scipy.optimize  as optimize
from numpy import  random as rn
from SterileDar import EventsnumberCC

evcc = EventsnumberCC.EventsnumberCC()
evt = InteractionSpectrum.Events()

int_err = 0.01
rn.seed(20210607)

# Energies for plotting
EnuPb = np.arange(ct.lead_min_e,ct.muonmass/2,.2)                   # for Lead

#Considering 208Pb (1ton) (desappearance)
ntotalve_osc_bf = [evcc.ntotalve(ct.Ue4_2,ct.Umu4_2,ct.DelM2)]

print("Configuração: Ue4={0}, Umu4={1}, DelM2={2}".format(ct.Ue4_2,ct.Umu4_2,ct.DelM2))
print("Número total de interações de neutrinos do elétron em um ano:{0}".format(ntotalve_osc_bf))

ntotalve_noosc = [evcc.ntotalve(0,0,0)]
print("Configuração: Ue4={0}, Umu4={1} DelM2={2}".format(0,0,0))
print("Número total de interações de neutrinos do elétron em um ano:{0}".format(ntotalve_noosc))

bins = np.linspace(ct.lead_min_e, ct.muonmass/2, 10+1 )
measured     = np.zeros(len(bins) - 1)
prediction   = np.zeros(len(bins) - 1)

for i in range(len(bins) - 1):
    if i == 6:
        measured[i] = rn.poisson([integrate.quad(lambda Enu1: evt.dNdEvee(Enu1,ct.Ue4_2,ct.DelM2), bins[i], bins[i+1], epsabs=int_err)][0][0] + evt.NMuOriginCC(ct.NuMuenergy,ct.Ue4_2,ct.Umu4_2,ct.DelM2))
    else:
        measured[i] = rn.poisson([integrate.quad(lambda Enu1: evt.dNdEvee(Enu1,ct.Ue4_2,ct.DelM2), bins[i], bins[i+1], epsabs=int_err)][0][0])
  

def chi2_disappearence(Ue4, Umu4, DelM2):
    """ This function calculates the chi2 for the nu_e disappearence channel on Pb 
    """
    chi2_val = 0.
    for i in range(len(bins) - 1 ):
        if i == 6:
            prediction[i] = [integrate.quad(lambda Enu1: evt.dNdEvee(Enu1,Ue4,DelM2), bins[i], bins[i+1], epsabs=int_err)][0][0] + evt.NMuOriginCC(ct.NuMuenergy,Ue4,Umu4,DelM2)
        else:
            prediction[i] = [integrate.quad(lambda Enu1: evt.dNdEvee(Enu1,Ue4,DelM2), bins[i], bins[i+1], epsabs=int_err)][0][0]
        chi2_val += ((measured[i]-prediction[i])**2)/prediction[i]
    return chi2_val

v_chi2 = np.vectorize(chi2_disappearence)

# plotting Chi2 as a function of Ue4

x_ue4 = np.linspace(0.001,0.05,100+1)
plt.title(r'Mínimo de $\chi^2$ em função de $|U_{e4}|^{2}$')
plt.xlabel(r'$|U_{e4}|^{2}$')
plt.ylabel(r'$\chi^2$')
plt.plot(x_ue4, v_chi2(x_ue4,ct.Umu4_2,ct.DelM2), 'r')
plt.show()

# find minimum of Chi2 as function of Ue4

def chi2_dis_ue4(Ue4):
    return chi2_disappearence(Ue4,ct.Umu4_2,ct.DelM2)

min_chi2_ue4 = optimize.minimize(chi2_dis_ue4, 0.02)
print(min_chi2_ue4)
print(min_chi2_ue4.x[0])
print(min_chi2_ue4.fun)

# find interval of Ue4

def chi2_dis_ue4_sig(Ue4):
    return chi2_dis_ue4(Ue4)-(min_chi2_ue4.fun+1)

sol1 = optimize.fsolve(chi2_dis_ue4_sig,min_chi2_ue4.x[0]+0.0001)
sol2 = optimize.fsolve(chi2_dis_ue4_sig,min_chi2_ue4.x[0]-0.0001)

print("limite superior intervalo confiança:", sol1)
print(chi2_dis_ue4(sol1[0]))
print("limite inferior intervalo confiança:", sol2)
print(chi2_dis_ue4(sol2[0]))