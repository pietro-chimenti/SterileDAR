 #Inverse beta decay cross section at zeroth order arxiv:9903554 equation (10)
import sys
sys.path.append("..")
from SterileDar import constants as ct
from SterileDar import crosssections
import numpy as np
import matplotlib.pyplot as plt

cs=crosssections.crosssections()

Enu= np.arange(ct.energythresholdIBD,ct.muonmass/2,.5)

plt.plot(Enu,cs.sigmaIBD(Enu),'r')
plt.grid(True)
plt.xlabel(r"Energia dos neutrinos [$MeV$]")
plt.ylabel(r"Seção de choque[$m^{2}$]")
plt.show()