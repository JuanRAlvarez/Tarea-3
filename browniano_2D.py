import numpy as np
import matplotlib.pyplot as plt
import sys

n_points = int(sys.argv[1])

a = 360*np.random.random(n_points)
x = np.zeros(n_points)
y = np.zeros(n_points)
lgn = np.zeros(n_points)
for i in range(n_points - 1):
    x[i+1] = x[i]+ np.cos(a[i])
    y[i+1] = y[i] + np.sin(a[i])
d = np.sqrt( x**2  + y**2)

u = np.linspace(0,15,20)

w = 0.5*u

plt.plot(np.log(range(n_points)),np.log(d))
plt.plot(u,w)
plt.xlabel("Log(n_puntos)")
plt.ylabel("Log(distancia)")
plt.title("Movimiento Browniano en 2 Dimensiones")
plt.savefig('browninano_2D_'+str(n_points)+'.pdf')

