#cross sections 208Pb based in arXiv:0209267
import sys
sys.path.append("..")
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from SterileDar import crosssections
import numpy as np
import matplotlib
#Use LaTeX
matplotlib.rcParams['text.usetex'] = True
#Figure config
figure(num=None, figsize=(10, 8), dpi=80, facecolor='w', edgecolor='k')
matplotlib.rcParams.update({'font.size': 16})

print("Gráfico das seções de choque de (anti)neutrinos com 208Pb via correntes carregada e neutra")

E = np.arange(5,100,5)

cs=crosssections.crosssections()

plt.title(u'Seções de choque')
plt.plot(E,cs.vee1n,'r',linewidth=1.0,label=r'$\nu_{e}+^{208}$Pb$\rightarrow ^{207}$Bi$+n+e^{-}$')
plt.plot(E,cs.vee2n,'b',linewidth=1.0,label=r'$\nu_{e}+^{208}$Pb$\rightarrow ^{206}$Bi$+2n+e^{-}$')
plt.plot(E,cs.veetotal,'g',linewidth=1.0,label=r'$\nu_{e} \rightarrow e^{-}$')
plt.plot(E,cs.vv1n,'c',linewidth=1.0,label=r'$\nu_{x}+^{208}$Pb$\rightarrow ^{207}$Pb$+n+\bar{\nu_{x}}$')
plt.plot(E,cs.vv2n,'m',linewidth=1.0,label=r'$\nu_{x}+^{208}$Pb$\rightarrow ^{207}$Pb$+2n+\bar{\nu_{x}}$')
plt.plot(E,cs.vvtotal,'y',linewidth=1.0,label=r'$\nu_{x} \rightarrow \nu_{x}$')
plt.plot(E,cs.vbarvbar1n,'k',linewidth=1.0,label=r'$\bar{\nu_{x}}+^{208}$Pb$\rightarrow ^{207}$Pb$+n+\bar{\nu_{x}}$')
plt.plot(E,cs.vbarvbar2n,'navy',linewidth=1.0,label=r'$\bar{\nu_{x}}+ ^{208}$Pb$\rightarrow ^{206}$Pb$+2n+\bar{\nu_{x}}$')
plt.plot(E,cs.vbarvbartotal,'deeppink',linewidth=1.0,label=r'$\bar{\nu_{x}} \rightarrow \bar{\nu_{x}}$')

plt.legend()
plt.grid(True)
plt.xlabel(r'Energia do (Anti)Neutrino [$MeV$]')
plt.ylabel(r'Seções de choque $[10^{-40} cm^{-2}]$')
#plt.savefig('SpecE.pdf')
plt.show()