#Energy spectra of the resulting neutrinos
from SterileDar import constants as ct

class Spectra:
    def __init__(self, *args, **kwargs):
	# you can add additional code here if needed
        pass
    
    def dGdEve(self,E):
        return (96*(E**2)*((ct.muonmass)-(2*E))/(ct.muonmass**4))
    
    def dGdEvmbar(self,E):
        return (16*(E**2)*((3*ct.muonmass)-(4*E)))/(ct.muonmass**4)

    def dGdEvm(self,E):
        return 1