#Targets number for experimental design of jsns2
import sys
sys.path.append("..")
from SterileDar import expdata as exp

print('Número total de átomos de carbono')
print(exp.carbonototal)
print('Número total de átomos de hidrogênio')
print(exp.hidrogeniototal)
print('Número total de átomos de nitrogênio')
print(exp.nitrogeniototal)
print('Número total de átomos de oxigênio')
print(exp.oxigeniototal)
print('Número de átomos de 208Pb em 1 ton')
print(exp.pbnumber)

