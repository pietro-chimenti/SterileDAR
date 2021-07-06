# This code prints the calculated number of targets in the experimental design of jsns2
# author: P. Chimenti, R.Bassi

from SterileDar import expdata as exp
import matplotlib.pyplot as plt
import numpy as np


#PPO/LAB/Paraffin
print('Número total de átomos de carbono')
print(exp.carbonototal)
print('Número total de átomos de hidrogênio')
print(exp.hidrogeniototal)
print('Número total de átomos de nitrogênio')
print(exp.nitrogeniototal)
print('Número total de átomos de oxigênio')
print(exp.oxigeniototal)
#208Pb
print('Número de átomos de 208Pb em 1 ton')
print(exp.pbnumber)


#=Table with information

fig = plt.figure(dpi=125, figsize=(8,8))
ax = fig.add_subplot(2,1,1)
table_data=[
    [r'Carbono', "{0}".format(np.format_float_scientific(exp.carbonototal,2))],
    [r'Hidrogênio', "{0}".format(np.format_float_scientific(exp.hidrogeniototal,2))],
    [r'Nitrogênio', "{0}".format(np.format_float_scientific(exp.nitrogeniototal,2))],
    [r'Oxigênio', "{0}".format(np.format_float_scientific(exp.oxigeniototal,2))],
    [r'208Pb em 1 ton', "{0}".format(np.format_float_scientific(exp.pbnumber,2))]      
]

table_label = ["Tipo de Átomo", "Número Total"]

ccolors = plt.cm.BuPu(np.full(len(table_label), 0.15))

table = ax.table(cellText=table_data, cellLoc='center', loc='center', colColours=ccolors, colLabels=table_label, edges='closed')
table.set_fontsize(14)
table.scale(1,2)
ax.axis('off')

plt.title('Número de Átomos no detector', pad=5)
plt.tight_layout()
plt.savefig('TargetsNumber.pdf')
#plt.show()