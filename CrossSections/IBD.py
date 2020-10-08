# -*- coding: utf-8 -*-

import sys
sys.path.append("..")
from SterileDar import constants as ct
import numpy as np
import math
import scipy.integrate as integrate
import matplotlib.pyplot as plt
import matplotlib as mpl

f=1
f2 = 3.706    
g = 1.26
deltainner = 0.024
Enu= np.arange(0,ct.muonmass/2,.5)
sigmazero = ((((ct.planckconstantcut**2)*(ct.lightconstant**2))*((ct.fermiconstant**2) * (ct.coscabibboangle**2))*(1+deltainner))/np.pi)
delta = (ct.neutronmass - ct.protonmass)
Massnp = ((ct.neutronmass + ct.protonmass)/2)

#Eezero = Enu - delta
#pezero = np.sqrt((Enu - delta)**2 - ct.electronmass**2)
#vezero = ( np.sqrt((Enu - delta)**2 - ct.electronmass**2) )/(Enu - delta)

def dsigmadcos(theta,Enu):
        return (sigmazero/2) * ((f**2 +3*g**2) + (f**2-g**2)*((np.sqrt(((Enu-delta)*((1-(Enu/Massnp)*(1-((np.sqrt((Enu-delta)**2-ct.electronmass**2))/(Enu-delta))*np.cos(theta))) -  ((delta**2 - ct.electronmass**2)/(2*Massnp))  ))**2 - ct.electronmass**2))/((Enu - delta )*(1 - (Enu/Massnp)*(1 - ( ( np.sqrt((Enu - delta)**2 - ct.electronmass**2) )/(Enu - delta) )*np.cos(theta))))*np.cos(theta))) * ((Enu-delta)*(1 - (Enu/Massnp)*(1-((np.sqrt((Enu-delta)**2-ct.electronmass**2))/(Enu-delta))*np.cos(theta))) -((delta**2 - ct.electronmass**2)/(2*Massnp))) * (np.sqrt(( ( Enu - delta )*(1 - (Enu/Massnp)*(1 - ( ( np.sqrt((Enu - delta)**2 - ct.electronmass**2) )/(Enu - delta) )*np.cos(theta))) -  ((delta**2 - ct.electronmass**2)/(2*Massnp))    )**2 - ct.electronmass**2)) \
            - (sigmazero/2) * ((2*(f+f2)*((2*( Enu - delta )+delta)*(1-( ( np.sqrt((Enu - delta)**2 - ct.electronmass**2) )/(Enu - delta) )*np.cos(theta))-((ct.electronmass**2)/( Enu - delta )))+(f**2+g**2)*((delta)*(1+( ( np.sqrt((Enu - delta)**2 - ct.electronmass**2) )/(Enu - delta) )*np.cos(theta))-((ct.electronmass**2)/( Enu - delta )))+(f**2+3*g**2)*((( Enu - delta )+delta)*(1-(np.cos(theta)/( ( np.sqrt((Enu - delta)**2 - ct.electronmass**2) )/(Enu - delta) )))-(delta))+(f**2-g**2)*((( Enu - delta )+delta)*(1-(np.cos(theta)/( ( np.sqrt((Enu - delta)**2 - ct.electronmass**2) )/(Enu - delta) )))-(delta))*(( ( np.sqrt((Enu - delta)**2 - ct.electronmass**2) )/(Enu - delta) )*np.cos(theta)))/Massnp)*\
                (Enu-delta)*(np.sqrt((Enu-delta)**2 - ct.electronmass**2))


result = [integrate.quad(lambda theta: dsigmadcos(theta,Enu), 0, 2*np.pi)
          for Enu in np.arange(0,ct.muonmass/2,.5)]

print(result)

#GAMA= 2*(f+f2)*((2*Eezero+delta)*(1-vezero*np.cos(theta))-((ct.electronmass**2)/Eezero))+(f**2+g**2)*((delta)*(1+vezero*np.cos(theta))-((ct.electronmass**2)/Eezero))+(f**2+3*g**2)*((Eezero+delta)*(1-(np.cos(theta)/vezero))-(delta))+(f**2-g**2)*((Eezero+delta)*(1-(np.cos(theta)/vezero))-(delta))*(vezero*np.cos(theta))

plt.plot(Enu,result)
plt.show()

print(ct.coscabibboangle)
#plt.xlabel("Valores de ka")
#plt.ylabel("Valores da integral")

#Ee1= Eezero*(1 - (Enu/Massnp)*(1 - vezero*np.cos(theta)))

#ve1= (pe1)/(Ee1)

#pe1= np.sqrt(Ee1**2 - ct.electronmass**2)