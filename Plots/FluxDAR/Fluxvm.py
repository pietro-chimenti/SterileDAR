# This code plots the flux as function of energy of the particles emitted in pion DAR, considering 24m
# author: P. Chimenti, R.Bassi

from SterileDar import DARSpectrum
from SterileDar import OscillationModel
from SterileDar import expdata as exp
from SterileDar import Flux
from SterileDar import constants as ct
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import numpy as np

spc = DARSpectrum.Spectra()
model = OscillationModel.OscillationModel()
flx = Flux.Flux()

int_err = 0.01

print("Gráfico do fluxo dos neutrinos por energia emitidos no DAR do pion+")

numberperyear = ([integrate.quad(lambda Enu: flx.Fluxvm(ct.Ljsns2,Enu,ct.Ue4_2,ct.Umu4_2,ct.DelM2), 0, ct.muonmass/2, epsabs=int_err, limit=15000)][0][0] + flx.nvmuvmu )
print(r"Número total de neutrinos do múon em um ano por metro quadrado: {:e}".format(numberperyear))

plt.rcParams.update({
    "figure.figsize": [8.0,6.0],
    "figure.dpi": 72.0,
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica"],
    "font.size": 16,
    "axes.titlepad": 25})

L = ct.Ljsns2 #int(input("Digite um valor para a distância: "))
E = np.arange(10e-15,ct.muonmass/2,0.01)

plt.plot(E,flx.Fluxvm(L,E,ct.Ue4_2,ct.Umu4_2,ct.DelM2),'r',linewidth=1.0)
plt.vlines(ct.NuMuenergy, (flx.Fluxvm(L,ct.NuMuenergy,ct.Ue4_2,ct.Umu4_2,ct.DelM2)), ((flx.Fluxvm(L,ct.NuMuenergy,ct.Ue4_2,ct.Umu4_2,ct.DelM2))+flx.nvmuvmu), colors='red')
plt.ylim((-0.002, max(flx.Fluxvm(L,E,ct.Ue4_2,ct.Umu4_2,ct.DelM2))+6e13))
plt.title(r'Fluxo de neutrinos do múon por energia emitidos para L={0}m'.format(L))
plt.grid(True)
textstr = '\n'.join((
    r'$|U_{{e4}}|^{{2}}$= {0}'.format(ct.Ue4_2),
    r'$|U_{{\mu 4}}|^{{2}}$= {0}'.format(ct.Umu4_2),
    r'$\Delta m^{{2}}$= {0}eV$^{{2}}$'.format(ct.DelM2)))
plt.text(2,0.9e14,textstr, fontsize = 16, bbox = dict(facecolor = 'white', alpha = 1))
plt.xlabel(r'Energia dos neutrinos [MeV]')
plt.ylabel(r' $\frac{N}{4 \pi L^{2} } \frac{dN}{dE}$ [$\nu$ MeV$^{-1}$m$^{-2}$]')
plt.tight_layout()
plt.savefig('NUmuFlux{0}m.pdf'.format(L))
#plt.show()