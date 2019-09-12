class Spectra:
	def __init__(self, *args, **kwargs):
	# you can add additional code here if needed
		pass

	Mu = 105.7 # Mev/c²

	def dGdEve(self,E):
		return (96*(E**2)*((self.Mu)-(2*E))/(self.Mu**4))

	def dGdEvmbar(self,E):
		return (16*(E**2)*((3*self.Mu)-(4*E))/(self.Mu**4))

	def dGdEvm(self,E):
		if any(E == 30):
			return 1
		else:
			return 0
