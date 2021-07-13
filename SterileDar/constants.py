import numpy as np

#constants package
class constants:
    def __init__(self, *args, **kwargs):
        # you can add additional code here if needed
        pass
    
fermiconstant = 1.1663787e-11 #Mev^-2
coscabibboangle = 0.974
neutronmass =  939.565413 #Mev
protonmass =  938.2720813 #Mev
electronmass = 0.5109989461 #Mev
muonmass = 105.6583755 #Mev
planckconstantcut = 6.582119514e-22 #Mev*s
lightconstant = 299792458 #m/s
planckcutlight = (299792458 * 6.582119514e-22) #m*MeV
mol = 6.02e23
energythresholdIBD = 1.807 #MeV
meter2tocm2 = 1e+4
cm2tometer2 = 1e-4
NuMuenergy = 30 #MeV
MeVtoJoule = 1.60218e-13 #Joule
neutrinoprobabilityconstant = 1.267

#mixing parameters
DelM2   = 1.7
Ue4_2   = 0.019
Umu4_2  = 0.015
Ut4_2   = 0.01

#Experimental data jsns2 (arXiv:1705.08629v1)
rjsns2 = (3.2)/2 #m (JSNS2)
hjsns2 = 2.5 #m (JSNS2)
Ljsns2 = 24 #source-detector distance in meters
estimatednumber = float((1.8e14)*4*np.pi*(2400)**2) #antimuon neutrinos per year jsns2

#EMin Pb data
lead_min_e = 5