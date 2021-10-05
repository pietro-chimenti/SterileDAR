import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd

def PWB(mu,b,n):
    return ((mu+b)**n)*((np.exp(-(mu+b)))/math.factorial(n))

N = float(input("Digite um valor para N inteiro:  "))

dataplot = []
for mu in np.arange(0,16,0.05):
    b  = 3.0
    CL = 0.9
    data = []
    mubest=[]
    Pnmu = []
    Pnmubest = []
    R = []

    for n in np.arange(0,40,1):
        Pnmu.append(round(PWB(mu,b,n),5))
        muvalues=[]
        for i in np.arange(0,10,0.01):
            muvalues.append(PWB(i,b,n))
        mubest.append((np.argmax(muvalues)/100))

        Pnmubest.append(round(PWB(mubest[n],b,n),5))

        R.append(round(Pnmu[n]/Pnmubest[n],3))
        data.append([n,Pnmu[n],mubest[n],Pnmubest[n],R[n]])
        
    df=pd.DataFrame(data,columns=["n","Pnmu","mubest","Pnmubest","R"])
    
    df.sort_values("R",ascending=False,inplace=True)
    
    soma = []
    Measuredn = []
    
    for i,j in zip(df['n'],df['Pnmu']):
        soma.append(j)
        Measuredn.append(i)
        if sum(soma) >= CL:
            break
    
    CLreal = sum(soma)
    
    nmin = min(Measuredn)
    nmax = max(Measuredn)
    

    dataplot.append([nmin,nmax,mu])

dfplot=pd.DataFrame(dataplot,columns=["nmin","nmax","mu"])

x0_plot=list(dfplot["nmin"])
x1_plot=list(dfplot["nmax"])
y_plot =list(dfplot["mu"])

MU = []
for index, row in dfplot.iterrows():
    if N > row["nmin"] and N < row["nmax"]:
        MU.append(row["mu"])
    else:
        pass


fig = plt.figure()
ax = fig.gca()
ax = fig.add_subplot(111)
ax.set_aspect(1)
ax.set_xticks(np.arange(0, 15, 1))
ax.set_yticks(np.arange(0, 15, 1))
plt.xlabel('Measured n')
plt.ylabel(r'Signal Mean $\mu$')

x1, x2 = N, N
y1, y2 = min(MU), max(MU)
plt.plot([x1, x2], [y1, y2], 'r')

plt.plot(x0_plot,y_plot)
plt.plot(x1_plot,y_plot)
plt.xlim(0, 15)
plt.ylim(0, 15)
plt.grid()
plt.show()

print("Para o valor N = {0}, os limites de confiança são {1} e {2}".format(N,y1,y2 ))

