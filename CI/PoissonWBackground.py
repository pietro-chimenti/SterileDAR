#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 14:31:20 2021

@author: P.Chimenti, B.Araujo, R.Bassi
"""

import numpy as np
from   matplotlib import pyplot as plt

from scipy.stats import poisson
from scipy.stats import gamma
from scipy.stats import nbinom

fig, ax = plt.subplots(1, 1)
mu = 200
mean, var, skew, kurt = poisson.stats(mu, moments='mvsk')
print(mean,var,skew,kurt)
x = np.arange(poisson.ppf(0.01, mu), poisson.ppf(0.99, mu))# first percentile to last percentile
ax.plot(x, poisson.pmf(x, mu), 'bo', ms=8, label='poisson pmf')
ax.vlines(x, 0, poisson.pmf(x, mu), colors='b', lw=5, alpha=0.5)
rv = poisson(mu)
ax.vlines(x, 0, rv.pmf(x), colors='k', linestyles='-', lw=1, label='frozen pmf')
ax.legend(loc='best', frameon=False)
#plt.show()
plt.clf()

fig, ax = plt.subplots(1, 1)
a = 2
b = 3
mean, var, skew, kurt = gamma.stats(a, moments='mvsk')
print(mean,var,skew,kurt)
mean, var, skew, kurt = gamma.stats(a, scale=b, moments='mvsk')
print(mean,var,skew,kurt)
x = np.linspace(gamma.ppf(0.01, a), gamma.ppf(0.99, a), 100)
ax.plot(x, gamma.pdf(x, a), 'r-', lw=5, alpha=0.6, label='gamma-a=2,b=1 pdf')
ax.plot(x, gamma.pdf(x, a, scale = b), 'r-', lw=5, alpha=0.6, label='gamma-a=2,b=3 pdf')
ax.legend(loc='best', frameon=False)
plt.show()

fig, ax = plt.subplots(1, 1)
n,p=5,0.5
mean, var, skew, kurt = nbinom.stats(n,p, moments='mvsk')
print(mean,var,skew,kurt)
start = nbinom.ppf(0.01, n,p)
stop  = nbinom.ppf(0.99, n,p)
x = np.linspace(nbinom.ppf(0.01, n,p), nbinom.ppf(0.99, n,p), num = int(stop-start+1))
print(x)
ax.plot(x, nbinom.pmf(x, n, p), 'bo', ms=8, label='nbinom pdf')
ax.plot(x, poisson.pmf(x, 5), 'ro', ms=8, label='poisson pdf')
ax.legend(loc='best', frameon=False)
plt.show()



