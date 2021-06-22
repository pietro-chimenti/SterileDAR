# This code prints the calculated number of targets in the experimental design of jsns2
# author: P. Chimenti, R.Bassi

from SterileDar import expdata as exp

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