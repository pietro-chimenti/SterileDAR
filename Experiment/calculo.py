# coding=utf-8
import sys
sys.path.append("..")
from SterileDar import expdata
import numpy as np

exp=expdata.expdata()

print('Número total de átomos de carbono')
print(exp.carbonototal)
print('Número total de átomos de hidrogênio')
print(exp.hidrogeniototal)
print('Número total de átomos de nitrogênio')
print(exp.nitrogeniototal)
print('Número total de átomos de oxigênio')
print(exp.oxigeniototal)


