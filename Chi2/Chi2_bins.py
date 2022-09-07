# This code plots histograms of both no oscillation and oscillation with the best fit and compare with data generated with a random number generator 
# Plot Chi2 with bins information
# author: P. Chimenti, R.Bassi

from SterileDar import constants as ct
from SterileDar import InteractionSpectrum
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import matplotlib.font_manager
from textwrap3 import wrap
from scipy.stats import chi2

np.random.seed(20210507)

evt = InteractionSpectrum.Events()
int_err = 0.01

# Energies for plotting
lead_min_e = 5
EnuPb = np.arange(lead_min_e,ct.muonmass/2,.2)  #Lead range

#Considering 208Pb (1ton) (desappearance)
ntotalve_osc_bf = [integrate.quad(lambda Enu1: evt.dNdEvee(Enu1,ct.Ue4_2,ct.DelM2), lead_min_e, ct.muonmass/2, epsabs=int_err)][0][0] + evt.NMuOriginCC(ct.NuMuenergy,ct.Ue4_2,ct.Umu4_2,ct.DelM2)

print(r"Configuração: Ue4={0}, Umu4={1} , DelM2={2}".format(ct.Ue4_2,ct.Umu4_2,ct.DelM2))
print(r"Número total de interações de neutrinos do elétron em um ano:{0}".format(ntotalve_osc_bf))

ntotalve_noosc = [integrate.quad(lambda Enu1: evt.dNdEvee(Enu1,0,0), lead_min_e, ct.muonmass/2, epsabs=int_err)][0][0]
print(r"Configuração: Ue4={0}, DelM2={1}".format(0,0))
print(r"Número total de interações de neutrinos do elétron em um ano:{0}".format(ntotalve_noosc))

bins     = np.linspace(lead_min_e, ct.muonmass/2, 10+1 )
measured = np.zeros(len(bins) - 1)
no_osc   = np.zeros(len(bins) - 1)
osc      = np.zeros(len(bins) - 1)



###################################### NO OSCILLATION #########################################

integral_noosc = []
for i in range(len(bins) - 1 ):
    no_osc[i] = [integrate.quad(lambda Enu1: evt.dNdEvee(Enu1,0,0), bins[i], bins[i+1], epsabs=int_err)][0][0] + evt.NMuOriginCC(ct.NuMuenergy,0,0,0)
    integral_noosc.append(no_osc[i])
    
samples_noosc = []
for i in range(len(bins) - 1):
    samples_noosc.append(np.random.poisson(integral_noosc[i],1)[0])



######################################## BEST FIT #############################################

integral_osc = []
for i in range(len(bins) - 1 ):
    if i == 5:
        osc[i] = [integrate.quad(lambda Enu1: evt.dNdEvee(Enu1,ct.Ue4_2,ct.DelM2), bins[i], bins[i+1], epsabs=int_err)][0][0] + evt.NMuOriginCC(ct.NuMuenergy,ct.Ue4_2,ct.Umu4_2,ct.DelM2)
    else:
        osc[i] = [integrate.quad(lambda Enu1: evt.dNdEvee(Enu1,ct.Ue4_2,ct.DelM2), bins[i], bins[i+1], epsabs=int_err)][0][0]
    integral_osc.append(osc[i])
    
samples_osc = []
for i in range(len(bins) - 1):
    samples_osc.append(np.random.poisson(integral_osc[i],1)[0])
    

###################################### CHI2 DEFINITION #########################################

def chi2_someconfig(Ue4, DelM2):
    """ Esta função bla bla bla
    """
    chi2 = 0.
    for i in range(len(bins) - 1 ):
        if i == 5:
            measured[i] = ([integrate.quad(lambda Enu1: evt.dNdEvee(Enu1,Ue4,DelM2), bins[i], bins[i+1], epsabs=int_err)][0][0] + evt.NMuOriginCC(ct.NuMuenergy,Ue4,ct.Umu4_2,DelM2))
        else:
            measured[i] = ([integrate.quad(lambda Enu1: evt.dNdEvee(Enu1,Ue4,DelM2), bins[i], bins[i+1], epsabs=int_err)][0][0])
        chi2+= ((measured[i] - no_osc[i])**2)/measured[i]
    return chi2

vchi2_someconfig = np.vectorize(chi2_someconfig)

print(r"Chi2({0},{1})={2}".format(0,0,chi2_someconfig(0,0)))
print(r"Chi2({0},{1})={2}".format(ct.Ue4_2,ct.DelM2,chi2_someconfig(ct.Ue4_2,ct.DelM2)))

########################################### PLOTS ##############################################

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica"],
    "font.size": 16,
    "axes.titlepad": 25})



plt.hist(bins[:-1], bins, weights=integral_noosc, color='salmon', label='Sem oscilação' )
plt.plot((bins[1:]+bins[:-1])/2,samples_noosc,"*", color='red', label='Amostra sem oscilação')
plt.hist(bins[:-1], bins, weights=integral_osc, color='skyblue', label='Com oscilação' )
plt.plot((bins[1:]+bins[:-1])/2,samples_osc,"*", color='blue', label='Amostra com oscilação')
plt.title(r'Histograma do número esperado de interações $\nu^{CC}_{e}$ com $^{208}$Pb')
textstr = '\n'.join((
    r'$|U_{{e4}}|^{{2}}$= {0}'.format(ct.Ue4_2),
    r'$|U_{{\mu 4}}|^{{2}}$= {0}'.format(ct.Umu4_2),
    r'$\Delta m^{{2}}$= {0}eV$^{{2}}$'.format(ct.DelM2)))
plt.text(4.2,270,textstr, fontsize = 16, bbox = dict(facecolor = 'white', alpha = 1))
plt.xlabel(r'Energia [MeV]')
plt.ylabel(r'Número Esperado de Interações')
plt.legend(loc=2, shadow=True)
plt.savefig('NUebins208Pb.pdf')
plt.show()
plt.close()



######################################### PLOT CHI2 ############################################


chi21sigma = chi2.ppf(0.6827, df=9)
chi22sigma = chi2.ppf(0.9545, df=9)
chi23sigma = chi2.ppf(0.9973, df=9)


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
ax.set_aspect(1)
ax.set_xscale("log") 
ax.set_yscale("log")
CS = ax.contour(Y, X, Z, levels = [chi21sigma,chi22sigma,chi23sigma] )
ax.clabel(CS, inline=1, fontsize=10)
ax.set_title(r'Plot de Sensibilidade $\nu_{e}^{CC}$ - $\chi^2$')
ax.set_xlabel(r'$sen^2 2\theta$')
ax.set_ylabel(r'$\Delta m^2$')
ax.scatter( (4*0.019*(1-0.019))  , 1.7 , c="red")
plt.grid(True)
plt.xlim([0.01,1])
plt.ylim([0.1,10])
plt.savefig('sensitivityNUedisappearencebins.pdf')
plt.show()

