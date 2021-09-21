import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd

def Gaussian(mu,x):
    return (1/np.sqrt(2*np.pi)) * np.exp(-(((x-mu)**2)/2))

def Rxn(mu,x):
    return np.exp(x*mu - (mu**2)/2)

def Rxp(mu,x):
    return np.exp(-(((x-mu)**2)/2))

def Pxmubestneg(x):
    return np.exp((-x**2)/2)/np.sqrt(2*np.pi)

Pxmubestpos = (1/(np.sqrt(2*np.pi)))
    
dataplot = []
for mu in np.arange(0,15,0.1):
    CL = 0.9
    data = []
    mubest=[]
    Pnmu = []
    Pnmubest = []
    R = []

    i=0

    for x in np.arange(-10,10,1):
        Pnmu.append(round(Gaussian(mu,x),5))        
        
        if x < 0:
            Pnmubest.append(round(Pxmubestneg(x),4))
            R.append(round(Rxn(mu, x),3))
             
        else :
            Pnmubest.append(round(Pxmubestpos,4))
            R.append(round(Rxp(mu, x),3))

            
        data.append([x,Pnmu[i],Pnmubest[i],R[i]])
        i+=1
        
        
    df=pd.DataFrame(data,columns=["x","Pnmu","Pnmubest","R"])
    
    df.sort_values("R",ascending=False,inplace=True)
    
    soma = []
    Measuredx = []
    
    for m,j in zip(df['x'],df['Pnmu']):
        soma.append(j)
        Measuredx.append(m)
        if sum(soma) >= CL:
            break
    
    CLreal = sum(soma)
    
    xmin = min(Measuredx)
    xmax = max(Measuredx)
    
    dataplot.append([xmin,xmax,mu])

dfplot=pd.DataFrame(dataplot,columns=["xmin","xmax","mu"])

x0_plot=list(dfplot["xmin"])
x1_plot=list(dfplot["xmax"])
y_plot =list(dfplot["mu"])


fig = plt.figure()
ax = fig.gca()
ax = fig.add_subplot(111)
ax.set_aspect(1)
ax.set_xticks(np.arange(-3, 5, 1))
ax.set_yticks(np.arange(-1, 7, 1))
plt.plot(x0_plot,y_plot)
plt.plot(x1_plot,y_plot)
plt.xlim(-2, 4)
plt.ylim(0, 6)
plt.grid()
plt.show()