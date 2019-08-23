import math

class OscillationModel:
    """ This class bla bla """

    DelM2 = 1.0
    Ue4   = 0.2
    Umu4  = 0.3

    
    def __init__(self, *args, **kwargs):
        # you can add additional code here if needed
        print("OScillation Model Contructor")

    def Pee(self,L,E):
        return 1.-4.*(1-self.Ue4**2)*(self.Ue4**2)*((math.sin(1.27*self.DelM2*L/E))**2)
