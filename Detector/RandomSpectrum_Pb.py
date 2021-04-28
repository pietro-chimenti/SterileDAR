import sys
sys.path.append("..")
import matplotlib.pyplot as plt
from SterileDar import constants as ct
from SterileDar import expdata as exp
from SterileDar import Events
import numpy as np
import scipy.integrate as integrate

np.random.seed(20210420)

evt = Events.Events()  # to import functions

bins = np.linspace(5,ct.muonmass/2,11) 
print(bins)

integrals = []
for i in range(10):
    result = integrate.quad(lambda x: evt.dNdEvee(x,10*ct.Ue4_2,ct.DelM2), bins[i], bins[i+1])
    integrals.append(result[0])

samples = []
for i in range(10):
    samples.append(np.random.poisson(integrals[i],1)[0])


print(integrals)
print(samples)


plt.hist(bins[:-1], bins, weights=integrals)
plt.plot((bins[1:]+bins[:-1])/2,samples,"*")
plt.show() 

def chi2( Ue4, DelM2 ):
    integrals_th = []
    chi2_th      = 0
    for i in range(10):
        result = integrate.quad(lambda x: evt.dNdEvee(x, Ue4, DelM2), bins[i], bins[i+1])
        integrals_th.append(result[0])
        #if samples[i] != 0 :        chi2_th += ((samples[i]-integrals_th[i])**2)/(samples[i])
        if samples[i] != 0 :        chi2_th += ((integrals[i]-integrals_th[i])**2)/(samples[i])
    return chi2_th

Ue4_fig   = np.arange(0.17,0.21,0.001)
Chi2_vals = []
for i in Ue4_fig:
    Chi2_vals.append(chi2(i,ct.DelM2))
    

plt.plot(Ue4_fig, Chi2_vals)
plt.show()

