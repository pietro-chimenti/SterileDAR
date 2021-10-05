import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd
from scipy import optimize
import scipy.integrate as integrate

def Gaussian(x,mu):
    return (1/np.sqrt(2*np.pi)) * np.exp(-(((x-mu)**2)/2))

def R(x,mu):
    if x < 0:
        return np.exp(x*mu - (mu**2)/2)
    else:
        return np.exp(-(((x-mu)**2)/2))

def R_r(x,mu,r):
    return R(x,mu) - r

def residualconfidence(r, alpha, mu):
    root_plus = optimize.bisect(R_r, mu, 10000, args=(mu, r, ))
    root_minus = optimize.bisect(R_r, -10000, mu, args=(mu, r, ))
    return integrate.quad(lambda x: Gaussian(x,mu), root_minus, root_plus)[0] - alpha
    
list_minus = []
list_plus = []

for mu in np.arange(0.001,6,0.1):
    alpha = 0.9
    
    r = optimize.bisect(residualconfidence, 0.0001, 0.9999, args=(alpha,mu, ))
    
    root_plus = optimize.bisect(R_r, mu, 10000, args=(mu, r, ))
    root_minus = optimize.bisect(R_r, -10000, mu, args=(mu, r, ))
    
    list_minus.append(root_minus)
    list_plus.append(root_plus)

mu = np.arange(0.001,6,0.1)

fig = plt.figure()
ax = fig.gca()
ax = fig.add_subplot(111)
ax.set_aspect(1)
ax.set_xticks(np.arange(-3, 5, 1))
ax.set_yticks(np.arange(-1, 7, 1))
plt.xlabel('Measured Mean x')
plt.ylabel(r'Mean $\mu$')

plt.plot(list_minus,mu)
plt.plot(list_plus,mu)
plt.xlim(-2, 4)
plt.ylim(0, 6)
plt.grid()
plt.show()

