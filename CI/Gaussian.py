import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st

confidence = (float(input("Insira a confiança de 0 a 100:  ")))/100
measured   = 0.02#np.random.normal() (float(input("Insira o valor medido:  ")))
mean       = measured
sigma = 1

#Calcutation

minc = measured + st.norm.ppf(1-(1+confidence)/2)
maxc = measured + st.norm.ppf(1-(1-confidence)/2)

ci = st.norm.interval(confidence, loc=measured, scale=sigma)

print("Para uma medida de {0}, Os limites de confiança são {1} e {2}".format(measured,ci[0],ci[1]))
print("Para uma medida de {0}, Os limites de confiança são {1} e {2}".format(measured,minc,maxc))

#Plot
plt.rcParams.update({
    "figure.figsize": [6.0,6.0],
    "figure.dpi": 72.0,
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica"],
    "font.size": 16,
    "axes.titlepad": 25})

x = np.arange(mean-4*sigma,mean+4*sigma,.01)
fig, ax = plt.subplots(1, 1)
ax.plot(x, st.norm.pdf(x, loc=measured, scale=sigma), 'k-', lw=2)


# confidence interval left line
one_x12, one_y12 = [ci[0],ci[0]], [0, st.norm.pdf(ci[0],loc=measured,scale=sigma)]
# confidence interval right line
two_x12, two_y12 = [ci[1],ci[1]], [0, st.norm.pdf(ci[1],loc=measured,scale=sigma)]
plt.plot(one_x12, one_y12, two_x12, two_y12, color='r')
# measured point
plt.plot(measured,0,'ro')
plt.show()

#Plot2

x1plot = []
x2plot = []

for medida in np.arange(0,7,1):
    ci = st.norm.interval(confidence, loc=medida, scale=sigma)
    x1plot.append(ci[0])
    x2plot.append(ci[1])

medida = [0,1,2,3,4,5,6]


fig = plt.figure()
ax = fig.gca()
ax = fig.add_subplot(111)
ax.set_aspect(1)
plt.plot(x1plot,medida,color='r')
plt.plot(x2plot,medida,color='r')
plt.ylim(0,6)
plt.xlim(-2,4)
plt.grid(True)
plt.xlabel(r'Medida de x')
plt.ylabel(r'Média $\mu$')

plt.title(r'Intervalo de Confiança Gaussiano Clássico')
#plt.savefig('cigaussian.pdf')
plt.show()