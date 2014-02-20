import numpy as np
import matplotlib.pyplot as plt
import sys

n_points = sys.argv[1]

a = 360*np.random.random(n_points)
x = np.zeros(n_points)
y = np.zeros(n_points)
lgn = np.zeros(n_points)
for i in range(n_points - 1):
    x[i+1] = x[i]+ np.cos(a[i])
    y[i+1] = y[i] + np.sin(a[i])
    lgn[i+1] = np.log(i+1)
d = np.sqrt( x**2  + y**2)

plt.pyplot.plot(range(n_points),d)
plt.pyplot.show()
