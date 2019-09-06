import numpy as np 

class OscillationModel:
	def __init__(self, *args, **kwargs):
	# you can add additional code here if needed
		pass

	DelM2 = 1.7 # eletron volts
	Ue4_2   = 0.019
	Umu4_2  = 0.015
	Mu = 105.7 # Mev/c²

	def Pee(self,L,E):
		return 1.-4.*(1-self.Ue4_2)*(self.Ue4_2)*((np.sin(1.27*self.DelM2*L/E))**2)

	def Pmm(self,L,E):
		return 1.-4.*(1-self.Umu4_2)*(self.Umu4_2)*((np.sin(1.27*self.DelM2*L/E))**2)

	def Pme(self,L,E):
		return 4.*(self.Umu4_2)*(self.Ue4_2)*((np.sin(1.27*self.DelM2*L/E))**2)

	def dGdEve(self,E):
		return (96*(E**2)*((self.Mu)-(2*E))/(self.Mu**4))

	def dGdEvam(self,E):
		return ((24*E*((3*self.Mu)-(4*E)))/(5*(self.Mu**3)))
