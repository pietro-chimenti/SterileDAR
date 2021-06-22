#Cross sections information and calculations

import sys
sys.path.append("..")
from SterileDar import constants as ct
import numpy as np
from scipy.interpolate import interp1d

#Necessary constants IBDcs calculation
f          = 1
f2         = 3.706    
g          = 1.26
delta      = (ct.neutronmass - ct.protonmass)
y2         = ( delta**2 - ct.electronmass**2 )/2
deltainner = 0.024
sigmazero  = ((((ct.planckconstantcut**2)*(ct.lightconstant**2))*((ct.fermiconstant**2) * (ct.coscabibboangle**2))*(1+deltainner))/np.pi)
Massnp     = 2*((ct.neutronmass + ct.protonmass)/2)

class crosssections:
    def __init__(self, *args, **kwargs):
        # you can add additional code here if needed
        pass

#IBD cross section at zeroth order arxiv:9903554 equation (10)
    def sigmaIBD(self,Enu):#Cross section IBD Simple cm^2
        return (sigmazero*(f**2+3*g**2)*(Enu - delta)*(np.sqrt((Enu - delta)**2 - ct.electronmass**2))) #m^2
    
#IBD cross section at first order arxiv:9903554 equation (14)

    def Eezero(self, Enu):
        return (Enu - delta)
    
    def pezero(self, Enu):
        return np.sqrt((Enu - delta)**2 - ct.electronmass**2)
    
    def vezero(self, Enu):
        return ( np.sqrt((Enu - delta)**2 - ct.electronmass**2) )/(Enu - delta)
    
    def Ee1(self, Enu, theta):
        return ((self.Eezero(Enu) * (1 - ( Enu / Massnp )*(1 - self.vezero(Enu) * np.cos(theta)))) - ( y2 / Massnp ))
    
    def pe1(self, Enu,theta):
        return np.sqrt((self.Ee1(Enu,theta)**2 - ct.electronmass**2))
    
    def ve1(self, Enu,theta):
        return (self.pe1(Enu,theta)) / (self.Ee1(Enu,theta))
    
    def GAMA(self, Enu,theta):
        return 2*( f + f2 ) * g * ((2*self.Eezero(Enu) + delta)*(1 - self.vezero(Enu) * np.cos(theta)) - ((ct.electronmass**2)/self.Eezero(Enu))) + (f**2+g**2)*(((delta)*(1+self.vezero(Enu)*np.cos(theta)))+((ct.electronmass**2)/self.Eezero(Enu))) + ( f**2 + 3*g**2)*((self.Eezero(Enu)+delta)*(1-(np.cos(theta)/self.vezero(Enu)))-(delta)) + (f**2 - g**2)*((self.Eezero(Enu)+delta)*(1 - (np.cos(theta)/self.vezero(Enu)))-(delta))*(self.vezero(Enu)*np.cos(theta))
    
    def dsigmadcos(self, theta, Enu):
        return (sigmazero/2 ) * (( f**2 + 3*g**2 ) + ( f**2 - g**2 ) * ( self.ve1(Enu,theta) ) * np.cos(theta) ) * self.Ee1(Enu, theta) * self.pe1(Enu,theta) - (sigmazero/2)*( self.GAMA(Enu,theta) / Massnp )*self.Eezero(Enu)*self.pezero(Enu)

#208Pb CS data based in arXiv:0209267
    E = np.arange(5,100,5) # to interpolate
    
    vee1n           = [0,.29e-11,.91,4.96,14.66,25.05,29.27,33.56,37.91,42.54,47.17,52.02,56.31,60.39,64.03,67.04,69.69,71.95,73.91]
    
    vee2n           = [0,0,0,0,.45,3.15,10.85,23.68,38.97,53.79,71.63,90.05,108.73,129.14,150.40,170.75,191.16,211.73,231.25]
    
    veetotal        = [.39e-7,0.09,1.54,6.51,17.63,32.22,45.37,64.10,85.33,106.16,130.09,154.64,178.75,204.17,229.88,253.92,277.58,300.95,323.03]
    
    vv1n            = [0,.002,.06,.20,.46,.87,1.44,2.15,2.97,3.86,4.79,5.74,6.71,7.69,8.67,9.65,10.58,11.45,12.23]
    
    vv2n            = [0,0,0,0,.03,.15,.42,.93,1.74,2.93,4.56,6.63,9.17,12.17,15.59,19.39,23.51,27.90,32.47]
    
    vvtotal         = [.67e-11,.007,.08,.27,.62,1.22,2.15,3.48,5.25,7.5,10.24,13.50,17.25,21.49,26.14,31.16,36.43,41.88,47.39]
    
    vbarvbar1n      = [0,.002,.05,.18,.40,.73,1.18,1.73,2.34,2.99,3.65,4.31,4.97,5.62,6.25,6.86,7.44,7.97,8.45]
    
    vbarvbar2n      = [0,0,0,0,.03,.13,.36,.76,1.39,2.26,3.42,4.85,6.54,8.47,10.62,12.94,15.39,17.93,20.51]
    
    vbarvbartotal   = [.66e-11,.007,.08,.24,.54,1.04,1.79,2.82,4.17,5.82,7.78,10.04,12.57,15.34,18.31,21.42,24.61,27.82,31.00]
    
    veetotal40      = [i*1e-40 for i in veetotal] #CC data electron neutrino e-40
    
    sigmaPbvee      = interp1d(E, veetotal40) #interpolated CS electron neutrino (CC interaction) [cm^2]
    
    vvtotal40       = [i*1e-40 for i in vvtotal]

    sigmaPbvv       = interp1d(E, vvtotal40) #interpolated CS neutrino (NC interaction) [cm^2]
    
    vbarvbartotal40 = [i*1e-40 for i in vbarvbartotal]
    
    sigmaPbvbarvbar = interp1d(E, vbarvbartotal40)  #interpolated CS neutrino (NC interaction) [cm^2]