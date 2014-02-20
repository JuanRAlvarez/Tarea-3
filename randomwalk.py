import numpy as np
import matplotlib as plt


n_points = 100000
a = 360*np.random.random(n_points)
x = zeros(n_points)
y = zeros(n_points)
lgn = zeros(n_points)
for i in range(n_points - 1):
    x[i+1] = x[i]+ np.cos(a[i])
    y[i+1] = y[i] + np.sin(a[i])
    lgn[i+1] = log(i+1)
d = np.sqrt( x**2  + y**2)


plt.plot(range(n_points),d)
