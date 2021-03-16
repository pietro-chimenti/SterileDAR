#Oscillation spectrum from each resulting neutrino
import sys
sys.path.append("..")
from SterileDar import Spectra
from SterileDar import OscillationModel

spc = Spectra.Spectra()
model = OscillationModel.OscillationModel()

class Oscspec:
        def __init__(self, *args, **kwargs):
        # you can add additional code here if needed
                pass

#oscillated spectrum of neutrinos
        def Oscspecve(self,L,E,Ue4_2,DelM2):
                return (spc.dGdEve(E)*model.Pee(L,E,Ue4_2,DelM2))

        def Oscspecvm(self,L,E,Ue4_2,Umu4_2,DelM2):
                return (spc.dGdEve(E)*model.Pme(L,E,Ue4_2,Umu4_2,DelM2))

        def Oscspecvt(self,L,E,Ue4_2,Ut4_2,DelM2):
                return (spc.dGdEve(E)*model.Pet(L,E,Ue4_2,Ut4_2,DelM2))

#oscillated spectrum of antineutrinos

        def Oscspecvmbar(self,L,E,Umu4_2,DelM2):
                return (spc.dGdEvmbar(E)*model.Pmm(L,E,Umu4_2,DelM2))

        def Oscspecvebar(self,L,E,Ue4_2,Umu4_2,DelM2):
                return (spc.dGdEvmbar(E)*model.Pme(L,E,Ue4_2,Umu4_2,DelM2))

        def Oscspecvtbar(self,L,E,Umu4_2,Ut4_2,DelM2):
                return (spc.dGdEvmbar(E)*model.Pmt(L,E,Umu4_2,Ut4_2,DelM2))