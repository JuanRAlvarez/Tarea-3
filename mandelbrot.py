import numpy as np
import matplotlib.pyplot as plt
import cmath
import sys
from pylab import *

iterations = int(sys.argv[1])

x = linspace(-2.5,1,1024)
y = linspace(-1,1,1024)
grid = zeros((1024,1024))
mandel_x = []
mandel_y = []

for i in range(1024):
    for j in range(1024):
        x0 =x[i]
        y0 =y[j]
        xp = 0.0
        yp = 0.0
        its = 0
        while (xp**2 + yp**2 < 4 and its < iterations):
            xtemp = xp**2 - yp**2 + x0
            yp = 2*xp*yp + y0
            xp = xtemp
            its = its + 1
        if its == iterations:
            mandel_x.append(x0)
            mandel_y.append(y0)

plt.plot(mandel_x,mandel_y,',k')
plt.xlabel("Re(z)")
plt.ylabel("Im(z)")
plt.title("Conjunto de Mandelbrot")
plt.savefig('mandelbrot_'+str(iterations)+'.pdf')
