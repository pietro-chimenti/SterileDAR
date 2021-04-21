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

