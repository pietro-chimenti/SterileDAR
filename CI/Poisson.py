import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st

confidence = (float(input("Insira a confiança de 0 a 100:  ")))/100

data = (float(input("Insira uma medida inteira positiva:  ")))

k = np.arange(data-12,data+12,1)

#Plotting

step = 0.01
param_points     = np.arange(0+step,100+step, step)
min_value_points = [ st.poisson.ppf(1-(1+confidence)/2, mu=val) for val in param_points ]
max_value_points = [ st.poisson.ppf(1-(1-confidence)/2, mu=val) for val in param_points ]

confidence_points = []
for i in range(len(param_points)):
    if min_value_points[i] < data and max_value_points[i] > data:
        confidence_points.append(param_points[i])

dots_x = np.ones(len(confidence_points))*data
dots_y = np.array(confidence_points)

plt.plot(max_value_points, param_points, color = 'blue')
plt.plot(min_value_points, param_points, color = 'red')
plt.plot(dots_x,dots_y,'ro')
plt.show()

print("Para uma medida de {0}, Os limites de confiança são {1} e {2}".format(data,dots_y[0],dots_y[-1]))


#Calcutation

minc = st.poisson.ppf(1-(1+confidence)/2, mu=data)
maxc = st.poisson.ppf(1-(1-confidence)/2, mu=data)

ci = st.poisson.interval(confidence, mu=data)

print("Para uma medida de {0}, Os limites de confiança são {1} e {2}".format(data,ci[0],ci[1]))
print("Para uma medida de {0}, Os limites de confiança são {1} e {2}".format(data,minc,maxc))

#Plot

plt.plot(k, st.poisson.pmf(k, mu=data), 'or', lw=1)



# confidence interval left line
one_x12, one_y12 = [ci[0],ci[0]], [0, 0.025]
# confidence interval right line
two_x12, two_y12 = [ci[1],ci[1]], [0, 0.025]
plt.plot(one_x12, one_y12, two_x12, two_y12, color='black')
# measured point
plt.plot(data,0,'bo') 


plt.show()

