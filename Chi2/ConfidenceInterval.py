# This code shows how many times the 'real' value of Ue4^2 is inside the confidence intervals of the simulations

import pandas as pd
from SterileDar import constants as ct
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager

#To read data and put in a dataframe
data10k = pd.read_csv("data10k.csv")
df = pd.DataFrame(data10k)

# To calculate how many times the value of Ue4^2 is inside the confidence intervals of the simulations
values = []

for i,j in zip(df['Confiança Inferior'],df['Confiança Superior']):
    if (i <= ct.Ue4_2) and (j >= ct.Ue4_2):
        values.append(i)
        
print("Ue4^2 está no intervalo de confiança simulado {0} vezes de uma amostra de 10000".format(len(values)))


# To plot a histogram of the simulated data of Ue4^2
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica"],
    "font.size": 16})

plt.title(r"Histograma de 10000 simulações")
plt.xlabel(r'Valor de $|U_{e4}|^{2}$')
plt.ylabel(r'Número de amostras')

plt.hist(df['Ue4^2'],bins=20,color='midnightblue',histtype='stepfilled',alpha=0.4, ec="k")
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
plt.show()