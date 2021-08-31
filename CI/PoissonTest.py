# To calculate how many times the parameter is inside the confidence intervals of the simulations
import pandas as pd

real = 50
numberofsamples = 10000

#To read data and put in a dataframe
data1 = pd.read_csv("data1-10k.csv")
df = pd.DataFrame(data1)

data2 = pd.read_csv("data2-10k.csv")
df2 = pd.DataFrame(data2)

values = []

for i,j in zip(df['minconfidence'],df['maxconfidence']):
    if (i <= real) and (j >= real):
        values.append(i)
        
print("No primeiro calculo o parâmetro está no intervalo de confiança simulado {0} vezes de uma amostra de {1}".format(len(values),numberofsamples))


# To calculate how many times the parameter is inside the confidence intervals of the simulations
values2 = []

for k,l in zip(df2['minconfidence'],df2['maxconfidence']):
    if (k <= real) and (l >= real):
        values2.append(k)
        
print("No segundo calculo o parâmetro está no intervalo de confiança simulado {0} vezes de uma amostra de {1}".format(len(values2),numberofsamples))    