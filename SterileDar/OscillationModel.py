#Survival and oscillation probabilities
import numpy as np 

class OscillationModel:
	def __init__(self, *args, **kwargs):
	# you can add additional code here if needed
		pass

	DelM2 = 1.7 # electron volts
	Ue4_2   = 0.019
	Umu4_2  = 0.015
	Ut4_2	= 0.01
	
	def Pee(self,L,E):
		return 1.-4.*(1-self.Ue4_2)*(self.Ue4_2)*((np.sin(1.27*self.DelM2*L/E))**2)

	def Pmm(self,L,E):
		return 1.-4.*(1-self.Umu4_2)*(self.Umu4_2)*((np.sin(1.27*self.DelM2*L/E))**2)

	def Pme(self,L,E):
		return 4.*(self.Umu4_2)*(self.Ue4_2)*((np.sin(1.27*self.DelM2*L/E))**2)

	def Pmt(self,L,E):
                return 4.*(self.Umu4_2)*(self.Ut4_2)*((np.sin(1.27*self.DelM2*L/E))**2)

	def Pet(self,L,E):
                return 4.*(self.Ue4_2)*(self.Ut4_2)*((np.sin(1.27*self.DelM2*L/E))**2)
