# This Code generates data with a random number generator
# author: P. Chimenti, R.Bassi

from SterileDar import constants as ct
from SterileDar import Events
import numpy as np
import scipy.integrate as integrate
import scipy.optimize  as optimize
from numpy import  random as rn
import pandas as pd
import time
start_time = time.time()


evt = Events.Events()

int_err = 0.01
#rn.seed(20210607)

#Minimum Energy Data 
lead_min_e = 6

#Considering 208Pb (1ton) (desappearance)
lista = [] #Result of each simulated experiment

for experiment in range(1):
    
    bins = np.linspace(lead_min_e, ct.muonmass/2, 10+1 )
    measured     = np.zeros(len(bins) - 1)
    prediction   = np.zeros(len(bins) - 1)
    

    # Here we simulate experimental data ("mock" data) 
    for i in range(len(bins) - 1):
        if i == 6:
            measured[i] = rn.poisson([integrate.quad(lambda Enu1: evt.dNdEvee(Enu1,ct.Ue4_2,ct.DelM2), bins[i], bins[i+1], epsabs=int_err)][0][0] + evt.NMuOriginCC(ct.NuMuenergy,ct.Ue4_2,ct.Umu4_2,ct.DelM2))
        else:
            measured[i] = rn.poisson([integrate.quad(lambda Enu1: evt.dNdEvee(Enu1,ct.Ue4_2,ct.DelM2), bins[i], bins[i+1], epsabs=int_err)][0][0])
      
    
    
    #Here we define the Chi^2
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
    

    # Find minimum of Chi2 as function of Ue4
    
    def chi2_dis_ue4(Ue4):
        return chi2_disappearence(Ue4,ct.Umu4_2,ct.DelM2)
    
    min_chi2_ue4 = optimize.minimize(chi2_dis_ue4, 0.02)

    
    # Find interval of Ue4
    
    def chi2_dis_ue4_sig(Ue4):
        return chi2_dis_ue4(Ue4)-(min_chi2_ue4.fun+1)
    
    sol1 = optimize.fsolve(chi2_dis_ue4_sig,min_chi2_ue4.x[0]+0.0001)
    sol2 = optimize.fsolve(chi2_dis_ue4_sig,min_chi2_ue4.x[0]-0.0001)
    
    lista.append([min_chi2_ue4.x[0],min_chi2_ue4.fun,sol2[0],sol1[0],chi2_dis_ue4(sol2[0]),chi2_dis_ue4(sol1[0])])
    print("{0} - {1} minutes ---".format(experiment,((time.time() - start_time)/60)))

df=pd.DataFrame(lista,columns=["Ue4^2","Chi2","Confiança Inferior","Confiança Superior", "Chi2(Inferior)", "Chi2(Superior)" ])
df.to_csv("data1.csv", index=False)
print(df)

print("--- %s minutes ---" % ((time.time() - start_time)/60))