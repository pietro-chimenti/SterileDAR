#Experimental data

import numpy as np
from SterileDar import constants as ct

class expdata:
	def __init__(self, *args, **kwargs):
       	# you can add additional code here if needed
               	pass
               
#Experimental data based arXiv:1908.03334
mmparafin = 352.68	#g/mol
dparafin = 900e3	#g/m³
mmlab = 260.46	#g/mol
dlab = 863e3	#g/m³
mmppo = 221.25	#g/mol
dppo = 1.1e6	#g/m³
    
#Experimental data jsns2 (arXiv:1705.08629v1)
rjsns2 = (3.2)/2 #m (JSNS2)
hjsns2 = 2.5 #m (JSNS2)
Ljsns2 = 24 #source-detector distance in meters
estimatedflux = float((1.8e14)*4*np.pi*(2400)**2) #antimuon neutrinos per year jsns2
    
#detector volume
vtotal=(np.pi)*(rjsns2**2)*hjsns2
vparafin=vtotal*0.15#m3
vppo=vtotal*0.003#m3
vlab=vtotal*0.847#m3
    
massparafin=vparafin*dparafin#g
massppo=vppo*dppo#g
masslab=vlab*dlab#g
    
molparafin=massparafin/mmparafin
molppo=massppo/mmppo
mollab=masslab/mmlab
    
moleculaparafin=ct.mol*molparafin
moleculappo=ct.mol*molppo
moleculalab=ct.mol*mollab
    
carbonoparafin=25*moleculaparafin
carbonolab=19*moleculalab
carbonoppo=15*moleculappo
carbonototal=carbonoparafin+carbonolab+carbonoppo
    
hidrogenioparafin=52*moleculaparafin
hidrogeniolab=32*moleculalab
hidrogenioppo=11*moleculappo
hidrogeniototal=hidrogenioparafin+hidrogeniolab+hidrogenioppo
    
nitrogeniototal=1*moleculappo
    
oxigeniototal=1*moleculappo

#Considering 208Pb
detectormass = 1000 #kg
atomicmass208pb = 207.9766521*1.66053906660e-27 #kg
pbnumber = (detectormass)/(atomicmass208pb)