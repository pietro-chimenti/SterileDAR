#Oscillation spectrum from each resulting neutrino
from SterileDar import Spectra
from SterileDar import OscillationModel

spc = Spectra.Spectra()
model = OscillationModel.OscillationModel()

class Oscspec:
        def __init__(self, *args, **kwargs):
        # you can add additional code here if needed
                pass

        def Oscspecve(self,L,E):
                return (spc.dGdEve(E)*model.Pee(L,E)+spc.dGdEvm(E)*model.Pme(L,E))

        def Oscspecvm(self,L,E):
                return (spc.dGdEve(E)*model.Pme(L,E)+spc.dGdEvm(E)*model.Pmm(L,E))

        def Oscspecvt(self,L,E):
                return (spc.dGdEve(E)*model.Pet(L,E)+spc.dGdEvm(E)*model.Pmt(L,E))

        def Oscspecvmbar(self,L,E):
                return (spc.dGdEvmbar(E)*model.Pmm(L,E))

        def Oscspecvebar(self,L,E):
                return (spc.dGdEvmbar(E)*model.Pme(L,E))

        def Oscspecvtbar(self,L,E):
                return (spc.dGdEvmbar(E)*model.Pmt(L,E))
            
        def Oscspecve1(self,L,E):
                return (spc.dGdEve(E)*model.Pee(L,E))
