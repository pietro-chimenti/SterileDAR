# Chi2 to test electron neutrino disappearence 
# author: P. Chimenti, R.Bassi
# date:   26/11/2020

import sys
sys.path.append("..")
from SterileDar import constants as ct
from SterileDar import expdata as exp
from SterileDar import Events
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate


evt = Events.Events()
int_err = 0.01

# Energies for plotting
lead_min_e = 6
Enu = np.arange(ct.energythresholdIBD,ct.muonmass/2,.2) # for IBD
EnuPb = np.arange(lead_min_e,ct.muonmass/2,.2)                   # for Lead

#Considering 208Pb (1ton) (desappearance)
ntotalve_osc_bf = [integrate.quad(lambda Enu1: evt.dNdEve(Enu1,ct.Ue4_2,ct.DelM2), lead_min_e, ct.muonmass/2, epsabs=int_err)]

print("Configuração: Ue4={0}, DelM2={1}".format(ct.Ue4_2,ct.DelM2))
print("Número total de interações de antineutrinos do elétron em um ano:{0}".format(ntotalve_osc_bf))

ntotalve_noosc = [integrate.quad(lambda Enu1: evt.dNdEve(Enu1,0,0), lead_min_e, ct.muonmass/2, epsabs=int_err)]
print("Configuração: Ue4={0}, DelM2={1}".format(0,0))
print("Número total de interações de antineutrinos do elétron em um ano:{0}".format(ntotalve_noosc))


def chi2_someconfig(Ue4, DelM2):
    """ Esta função bla bla bla
    """
    ntotalve = [integrate.quad(lambda Enu1: evt.dNdEve(Enu1,Ue4,DelM2), lead_min_e, ct.muonmass/2, epsabs=int_err)]
    chi2 = ((ntotalve[0][0] - ntotalve_noosc[0][0])**2)/ntotalve_noosc[0][0]
    return chi2

vchi2_someconfig = np.vectorize(chi2_someconfig)

print("Chi2({0},{1})={2}".format(0,0,chi2_someconfig(0,0)))
print("Chi2({0},{1})={2}".format(ct.Ue4_2,ct.DelM2,chi2_someconfig(ct.Ue4_2,ct.DelM2)))

# now plotting
import matplotlib.cm as cm


delta1 = 0.02
delta2 = 0.02
log_delm2    = np.arange(-1, 1., delta1)
log_sin22t   = np.arange(-2, 0., delta2)
delm2  = 10**log_delm2
sin22t = 10**log_sin22t
X, Y = np.meshgrid(delm2, sin22t)
ue4_2    = (1.-np.sqrt(1-Y))/2.
Z = vchi2_someconfig(ue4_2,X)
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica"]})
fig, ax = plt.subplots()
ax.set_xscale("log") 
ax.set_yscale("log") 
CS = ax.contour(Y, X, Z, levels = [1.,9.,25.] )
ax.clabel(CS, inline=1, fontsize=10)
ax.set_title(r'Sensitivity plot $\nu_e$ disappearence - Chi$^2$')
ax.set_xlabel(r'$sin^2 2\theta$')
ax.set_ylabel(r'$\Delta m^2$')
ax.scatter( (4*0.019*(1-0.019))  , 1.7 , c="red")
plt.grid(True)
plt.xlim([0.01,1])
plt.ylim([0.1,10])
plt.show()




