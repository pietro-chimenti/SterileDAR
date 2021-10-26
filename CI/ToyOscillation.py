#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 13:30:04 2021

@author: P.Chimenti, R.Bassi, B.Araujo
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson
import scipy.integrate as integrate
from scipy.optimize import minimize

# Here we define initial constants
class CommonConstants():
    E0   = 2
    Emax = 10
    L = 1
    Bins = 8
    Bins_limits = np.array([2,3,4,5,6,7,8,9,10])

    def __init__(self):
        pass
cc = CommonConstants()

def InitSpectrum(E):
    """ This function describe the initial unoscillated neutrino spectrum. 
    We consider a simple exponential.
    E : neutrino energy"""
    return np.exp(-E)

    
def OscProb(E, L, DelM2, S22t):
    """ This function represents the antineutrino survival probability. 
    E: neutrino energy
    L     : source-detector distance
    DelM2 : M^2_2-M^2_1
    S22t  : Sin^2(2 theta) """
    return 1-S22t*(np.sin(1.27*DelM2*L/E))**2

def CrossSect(E):
    """ This function is a "Toy" cross section inspired to the IBD cross section.
    Sigma = E*sqrt(E-E0)
    E0 = 1.8 is the threshold
    E : neutrino energy """
    return E*np.sqrt(E-cc.E0)

def Spectrum(E, L, DelM2, S22t):
    """ This function describes the oscillated spectrum.
    It is notmalized to have about 1000 events if no oscillation """
    K = 2083.81 # to get 1000 events if no oscillation
    return K*InitSpectrum(E)*CrossSect(E)*OscProb(E,L,DelM2,S22t)

def BinsMean(DelM2, S22t):
    """ This function calculate the expected stectrum in all bins """
    func = lambda x: Spectrum(x, cc.L, DelM2, S22t)
    means = np.array([integrate.quad(func,cc.Bins_limits[i],cc.Bins_limits[i+1], epsabs=1e-5)[0] for i in range(cc.Bins) ])
    return means

def RandomSample(DelM2, S22t):
    sample = np.array([ np.random.poisson(i)  for i in BinsMean(DelM2,S22t)])
    return sample

def LogLikelihood(pars, data):
    DelM2 = pars[0]
    S22t  = pars[1]
    means  = BinsMean(DelM2, S22t)
    binsLogLike = np.array([ -2.*(np.log(poisson.pmf(data[i],means[i]))) for i in np.arange(len(data)) ] )
    ll = sum(binsLogLike)
    return ll

def R(DelM2, S22t, data):
    bnds = ((0.1, 10), (0, 1))
    BestParams = minimize(LogLikelihood,(DelM2,S22t),args=(sample,),method='TNC', bounds=bnds, tol=1e-5).x
    R = np.exp(-LogLikelihood((DelM2,S22t),data)/2 + LogLikelihood(BestParams,data)/2)
    return R

DelM2 = 1
E = 2
S22t = 0.5


x_vals     = np.arange(cc.E0,10.,0.1)
y_vals     = Spectrum(x_vals, cc.L, DelM2, 0)    # no oscillation
y_vals_osc = Spectrum(x_vals, cc.L, DelM2, S22t) # oscillated
plt.plot(x_vals,y_vals)
plt.plot(x_vals,y_vals_osc)
plt.plot(x_vals,1000*InitSpectrum(x_vals))
plt.plot(x_vals,10*CrossSect(x_vals))
#plt.show()
plt.clf()

plt.hist(cc.Bins_limits[:-1],bins = cc.Bins_limits, weights = BinsMean(DelM2,0))
plt.plot((cc.Bins_limits[:-1]+cc.Bins_limits[1:])/2, RandomSample(DelM2,0),'o')
plt.hist(cc.Bins_limits[:-1],bins = cc.Bins_limits, weights = BinsMean(DelM2,S22t))
plt.plot((cc.Bins_limits[:-1]+cc.Bins_limits[1:])/2, RandomSample(DelM2,S22t),'*')
#plt.show()
plt.clf()


nsamples = 100
r_vals = np.zeros(nsamples)
for i in np.arange(nsamples):
    sample = RandomSample(DelM2, S22t)
    r_vals[i] = R(DelM2,S22t,sample)
    
plt.hist(r_vals,bins = np.arange(-0.5,1.2+0.01,0.01))
plt.show()

#########################################################################################
DelM2 = 1
E = 2
S22t = 0

nsamples = 100
r_vals = np.zeros(nsamples)
for i in np.arange(nsamples):
    sample = RandomSample(DelM2, S22t)
    r_vals[i] = R(DelM2,S22t,sample)
    
plt.hist(r_vals,bins = np.arange(-0.5,1.2+0.01,0.01))
plt.show()

#########################################################################################
DelM2 = 1
E = 2
S22t = 1

nsamples = 100
r_vals = np.zeros(nsamples)
for i in np.arange(nsamples):
    sample = RandomSample(DelM2, S22t)
    r_vals[i] = R(DelM2,S22t,sample)
    
plt.hist(r_vals,bins = np.arange(-0.5,1.2+0.01,0.01))
plt.show()

#########################################################################################
DelM2 = 0.1
E = 2
S22t = 1

nsamples = 100
r_vals = np.zeros(nsamples)
for i in np.arange(nsamples):
    sample = RandomSample(DelM2, S22t)
    r_vals[i] = R(DelM2,S22t,sample)
    
plt.hist(r_vals,bins = np.arange(-0.5,1.2+0.01,0.01))
plt.show()

#########################################################################################
DelM2 = 10
E = 2
S22t = 1

nsamples = 100
r_vals = np.zeros(nsamples)
for i in np.arange(nsamples):
    sample = RandomSample(DelM2, S22t)
    r_vals[i] = R(DelM2,S22t,sample)
    
plt.hist(r_vals,bins = np.arange(-0.5,1.2+0.01,0.01))
plt.show()


#print(R(DelM2,S22t,sample))
# parameter values
# DelM2    S22t
#  1         0
#  1         1
#  0.1       1
#  10        1