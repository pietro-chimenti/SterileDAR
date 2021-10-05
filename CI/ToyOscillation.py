#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 13:30:04 2021

@author: P.Chimenti, R.Bassi, B.Araujo
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate

# Here we define initial constants
E0   = 2
Emax = 10
L = 1
Bins = 8
Bins_limits = [2,3,4,5,6,7,8,9,10]

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
    return E*np.sqrt(E-E0)

def Spectrum(E, L, DelM2, S22t):
    """ This function describes the oscillated spectrum.
    It is notmalized to have about 1000 events if no oscillation """
    K = 2083.81 # to get 1000 events if no oscillation
    return K*InitSpectrum(E)*CrossSect(E)*OscProb(E,L,DelM2,S22t)

def BinsMean(DelM2, S22t):
    """ This function calculate the expected stectrum in all bins """
    func = lambda x: Spectrum(x, L, DelM2, S22t)
    means = [integrate.quad(func,Bins_limits[i],Bins_limits[i+1])[0] for i in range(Bins) ]
    return means

DelM2 = 1
E = 2
S22t = 0.5

print(round(InitSpectrum(E),3), round(OscProb(E,L,DelM2,S22t),3), round(CrossSect(E),3))

x_vals     = np.arange(E0,10.,0.1)
y_vals     = Spectrum(x_vals, L, DelM2, 0)    # no oscillation
y_vals_osc = Spectrum(x_vals, L, DelM2, S22t) # oscillated
plt.plot(x_vals,y_vals)
plt.plot(x_vals,y_vals_osc)
plt.plot(x_vals,1000*InitSpectrum(x_vals))
plt.plot(x_vals,10*CrossSect(x_vals))
plt.show()

plt.hist(Bins_limits[:-1],bins = Bins_limits, weights = BinsMean(DelM2,0))
plt.hist(Bins_limits[:-1],bins = Bins_limits, weights = BinsMean(DelM2,S22t))
plt.show()

print(sum(y_vals)*0.1)


