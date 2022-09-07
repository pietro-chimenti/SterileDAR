# This code shows how many times the 'real' value of Ue4^2 is inside the confidence intervals of the simulations

import pandas as pd
from SterileDar import constants as ct
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager
from scipy.stats import chi2

#To read data and put in a dataframe
data10k = pd.read_csv("data10k90.csv")
df = pd.DataFrame(data10k)

# To calculate how many times the value of Ue4^2 is inside the confidence intervals of the simulations
values = []

for i,j in zip(df['Confiança Inferior'],df['Confiança Superior']):
    if (i <= ct.Ue4_2) and (j >= ct.Ue4_2):
        values.append(i)
        
print("Ue4^2 está no intervalo de confiança simulado {0} vezes de uma amostra de 10000".format(len(values)))

chi2critval = np.quantile(df['Chi2'], 0.9)

chi2crit = chi2.ppf(0.9, df=9)

# To plot a histogram of the simulated data of Ue4^2
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica"],
    "font.size": 16})

plt.title(r"Histograma de 10K simulações")
plt.xlabel(r'Valor de $|U_{e4}|^{2}$')
plt.ylabel(r'Número de amostras')
plt.hist(df['Ue4^2'],bins=100,color='midnightblue',histtype='stepfilled',alpha=0.4, ec="k")
plt.savefig('10kUe4.pdf')
plt.show()


x_chi2 = np.linspace(0,52,101)
plt.plot(x_chi2 ,chi2.pdf(x_chi2,9), label='$\chi^{2}$ teórica', color='r')
plt.plot([chi2critval,chi2critval],[0,0.1],'black',label=r'90\% dos dados')
plt.plot([chi2crit,chi2crit],[0,0.1],'r--',label=r'Valor $\chi_{crit}^{2}$ 90\%')
plt.title(r'Histograma da distribuição de $\chi^{2}$ para 10K amostras')
plt.xlabel(r'Valor de $\chi^{2}$')
plt.ylabel(r'Frequência de Observação')
plt.hist(df['Chi2'],bins=100,density=True,color='midnightblue',histtype='stepfilled',alpha=0.4, ec="k", label='Dados Simulados')
plt.legend()
plt.savefig('chi2withOsc.pdf')
plt.show()




# To describe the statistics of the simulation
print(df['Ue4^2'].describe())


# To plot a mean of the Ue4^2 simulated data versus the number of samples
ue4 = []

for k in range(10000):
    ue4.append(df['Ue4^2'].sample(n=k, random_state=1).mean())

plt.plot(ue4, color='r', linewidth=1.0)
plt.yticks(np.arange(0.015, 0.022, step=0.0005))
plt.title(r"Variação da Média de $|U_{e4}|^{2}$")
plt.xlabel(r'Número de Simulações')
plt.ylabel(r'Média de $|U_{e4}|^{2}$')
plt.grid(True)
plt.savefig('10kMeanUe4.pdf')
plt.show()