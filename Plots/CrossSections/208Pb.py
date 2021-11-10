# This code plots the 208Pb cross sections based in arXiv:0209267
# author: P. Chimenti, R.Bassi

import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from SterileDar import crosssections
import numpy as np
import matplotlib
import matplotlib.font_manager

#Use LaTeX
matplotlib.rcParams['text.usetex'] = True
#Figure config
figure(num=None, figsize=(10, 8), dpi=80, facecolor='w', edgecolor='k')
matplotlib.rcParams.update({'font.size': 20})


print("Gráfico das seções de choque de (anti)neutrinos com 208Pb via correntes carregada e neutra")

E = np.arange(5,100,5)

cs=crosssections.crosssections()

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica"]})
plt.title(r'Seções de choque $^{208}$Pb')
plt.plot(E,cs.vee1n,'r',linewidth=1.0,label=r'$\nu_{e}+^{208}$Pb$\rightarrow ^{207}$Bi$+n+e^{-}$')
plt.plot(E,cs.vee2n,'b',linewidth=1.0,label=r'$\nu_{e}+^{208}$Pb$\rightarrow ^{206}$Bi$+2n+e^{-}$')
plt.plot(E,cs.veetotal,'g',linewidth=1.0,label=r'$\nu_{e} \rightarrow e^{-}$ (Todos os canais)')
plt.plot(E,cs.vv1n,'c',linewidth=1.0,label=r'$\nu_{x}+^{208}$Pb$\rightarrow ^{207}$Pb$+n+\nu_{x}$')
plt.plot(E,cs.vv2n,'m',linewidth=1.0,label=r'$\nu_{x}+^{208}$Pb$\rightarrow ^{207}$Pb$+2n+\nu_{x}$')
plt.plot(E,cs.vvtotal,'gold',linewidth=1.0,label=r'$\nu_{x} \rightarrow \nu_{x}$ (Todos os canais)')
plt.plot(E,cs.vbarvbar1n,'salmon',linewidth=1.0,label=r'$\overline{\nu}_{x}+^{208}$Pb$\rightarrow ^{207}$Pb$+n+\overline{\nu}_{x}$')
plt.plot(E,cs.vbarvbar2n,'black',linewidth=1.0,label=r'$\overline{\nu}_{x}+ ^{208}$Pb$\rightarrow ^{206}$Pb$+2n+\overline{\nu}_{x}$')
plt.plot(E,cs.vbarvbartotal,'darkgrey',linewidth=1.0,label=r'$\overline{\nu}_{x} \rightarrow \overline{\nu}_{x}$ (Todos os canais)')

plt.legend()
plt.grid(True)
plt.xlabel(r'Energia do (Anti)Neutrino [MeV]')
plt.ylabel(r'Seções de choque $[10^{-40} cm^{2}]$')
plt.tight_layout()
plt.savefig('CS_208Pb.pdf')
#plt.show()