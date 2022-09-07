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
import pandas as pd
import time
start_time = time.time()

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
    sample = np.array([ np.random.poisson(i) for i in BinsMean(DelM2,S22t)])
    return sample

def LogLikelihood(pars, data):
    DelM2 = pars[0]
    S22t  = pars[1]
    means  = BinsMean(DelM2, S22t)
    binsLogLike = np.array([ -2.*(np.log(poisson.pmf(data[i],means[i]))) for i in np.arange(len(data)) ] )
    ll = sum(binsLogLike)
    return ll

def R(DelM2, S22t, data):
    bnds = ((0.1, 100), (0, 1))
    BestParams = minimize(LogLikelihood,(DelM2,S22t),args=(sample,), method='TNC', bounds=bnds, tol=1e-5).x
    R = LogLikelihood((DelM2,S22t),data) - LogLikelihood(BestParams,data)
    return R

def R1(DelM2, S22t, data):
    bnds = ((0.1, 100), (0, 1))
    BestParams = minimize(LogLikelihood,(DelM2,S22t),args=(measurebins,),method='TNC', bounds=bnds, tol=1e-5).x
    R1 = LogLikelihood((DelM2,S22t),data) - LogLikelihood(BestParams,data)
    return R1

# =============================================================================
# x_vals     = np.arange(cc.E0,10.,0.1)
# y_vals     = Spectrum(x_vals, cc.L, DelM2, 0)    # no oscillation
# y_vals_osc = Spectrum(x_vals, cc.L, DelM2, S22t) # oscillated
# plt.plot(x_vals,y_vals)
# plt.plot(x_vals,y_vals_osc)
# plt.plot(x_vals,1000*InitSpectrum(x_vals))
# plt.plot(x_vals,10*CrossSect(x_vals))
# plt.show()
# plt.clf()
# 
# plt.hist(cc.Bins_limits[:-1],bins = cc.Bins_limits, weights = BinsMean(DelM2,0))
# plt.plot((cc.Bins_limits[:-1]+cc.Bins_limits[1:])/2, RandomSample(DelM2,0),'o')
# plt.hist(cc.Bins_limits[:-1],bins = cc.Bins_limits, weights = BinsMean(DelM2,S22t))
# plt.plot((cc.Bins_limits[:-1]+cc.Bins_limits[1:])/2, RandomSample(DelM2,S22t),'*')
# plt.show()
# plt.clf()
# 
# =============================================================================

################################# Chi2Crit Calculation #######################################
E = 2

DelM2values   = [ 1e-1,  1e0,  1e1,1e2 ]
Sen22tvalues  = [ 1e-3, 1e-2, 1e-1, 1  ]

chi2critlist  = []
delm2 = []
sen22t = []
delm2r = []
sen22tr = []
Rvalues = []
critquantile = []

nsamples = 3

for k in DelM2values:
    for j in Sen22tvalues:    
        r_vals = np.zeros(nsamples)
        for i in np.arange(nsamples):
            sample = RandomSample(k, j)
            r_vals[i] = R(k,j,sample)
            Rvalues.append(r_vals[i])
            sen22tr.append(j)
            delm2r.append(k)
            print("{0} - {1} minutes ---".format(i,((time.time() - start_time)/60)))
            
        chi2critvals = np.quantile(r_vals, 0.9)
        critquantile.append(chi2critvals)
        
        selectchi2 = pd.DataFrame(r_vals,columns=["Chi2 Values"])
        selectchi2.sort_values("Chi2 Values",ascending=True,inplace=True)
        
        chi290 = selectchi2.head(int(nsamples*0.9))
    
        chi2critvalue = (chi290.tail(1)).iloc[0]['Chi2 Values']
        
        delm2.append(k)
        sen22t.append(j)
        chi2critlist.append(chi2critvalue)

        del selectchi2


# =============================================================================
# datacrit = {'DelM2': delm2, 'Sen22t': sen22t, 'Chi2crit': chi2critlist, 'Chi2crit': chi2critlist, 'Chi2critquantile': critquantile}
# dfcrit   = pd.DataFrame(datacrit)
# dfcrit.to_csv("2datachi2crit1k.csv", index=False)
# =============================================================================


################################ PLOT R SIMULATION WITH CHI2CRIT #######################################

Rcol = {'DelM2':delm2r, 'Sen22t':sen22tr, 'Rvals':Rvalues}
Rdata = pd.DataFrame(Rcol)

index = -1
for i in Rdata['DelM2'].unique():
    for j in Rdata['Sen22t'].unique():
        index += 1
        Rvals = Rdata[(Rdata['DelM2']==i) & (Rdata['Sen22t']==j)]
        y, x, _ = plt.hist(Rvals['Rvals'],bins=nsamples)
        plt.plot([chi2critlist[index],chi2critlist[index]],[0,(np.array(y)).max()],'r')
        plt.plot([critquantile[index],critquantile[index]],[0,(np.array(y)).max()],'black')
        
        textstr = '\n'.join((
        r'$\Delta m^{{2}}$= {0}'.format(i),
        r'$sen^{{2}}2\theta$= {0}'.format(j)))
        plt.text(((np.array(x)).max()*0.75),(((np.array(y)).max())*0.9),textstr, fontsize = 16, bbox = dict(facecolor = 'white', alpha = 1))
        
        #plt.savefig('plotsR/plotdelm2{0}sen22t{1}.pdf'.format(i,j))
        plt.show()
        

################################ READ CSV TO COMPARE WITH CHI2 #######################################

data1k = pd.read_csv("2datachi2crit1k.csv")
dfcrit = pd.DataFrame(data1k)


################################## Chi2 Calculation ############################################

chimeasured  = []
sen22tt = []
delm2tt = []
critquantilett = []

experiment = 16

DelM2Measured  = [10]
Sen22tMeasured = [0.01]

for k in DelM2Measured:
    for j in Sen22tMeasured:
        r_vals = np.zeros(experiment)
        for i in np.arange(experiment):
            sample = np.round(BinsMean(k, j))
            r_vals[i] = R(k,j,sample)
            chimeasured.append(r_vals[i])
            sen22tt.append(j)
            delm2tt.append(k)

chi2c = np.quantile(chimeasured, 0.9)

for i in range(len(dfcrit['DelM2'])):
    critquantilett.append(chi2c)
            
datachi = {'DelM2': delm2, 'Sen22t': sen22t, 'Chi2': critquantilett}
dfchi  = pd.DataFrame(datachi)

datafull = {'DelM2': delm2, 'Sen22t': sen22t, 'Chi2 Critico': dfcrit['Chi2crit'], 'Chi2': critquantilett}
dffull  = pd.DataFrame(datafull)


plt.plot(np.round(BinsMean(1,0)),'r')
plt.plot((BinsMean(1,1)),'b')

plt.show()

print('chi2')
print(R(1,1,np.round(BinsMean(0,1))))



delm2plot  = []
sen22tplot = []
for deltam2,sen22t,chicrit,chi in zip(dffull['DelM2'],dffull['Sen22t'],dffull['Chi2 Critico'],dffull['Chi2']):
    if (chi < chicrit):
        delm2plot.append(deltam2)
        sen22tplot.append(sen22t)
    else:
        pass

alloweddata = {'DelM2': delm2plot, 'Sen22t': sen22tplot}
allowedpoints  = pd.DataFrame(alloweddata)


##################################### PLOT ALLOWED REGION ############################################

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set_yscale('log')
ax.set_xscale('log')
plt.plot(allowedpoints['Sen22t'],allowedpoints['DelM2'],'ro')
plt.show()


#X, Y = np.meshgrid(DelM2values , Sen22tvalues)


#print(R(DelM2,S22t,sample))
# parameter values
# DelM2    S22t
#  1         0.5
#  1         0
#  1         1
#  0.1       1
#  10        1