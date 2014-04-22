import numpy as np
import matplotlib.pyplot as plt
import sys

n_photons = int(sys.argv[1])
numbers = np.zeros(n_photons)
radius = 100

for j in range(n_photons):
    i=0
    x=np.empty((0))
    y=np.empty((0))
    z=np.empty((0))
    d=np.empty((0))

    x = np.append(x,0)
    y = np.append(y,0)
    z = np.append(z,0)
    d = np.append(d,0)

    while(d[i]<radius):

        a=np.pi*2*np.random.random()
        b=np.pi*np.random.random()
        x = np.append(x,x[i]+np.cos(a)*np.sin(b))
        y = np.append(y,y[i]+np.sin(a)*np.sin(b))
        z = np.append(z,z[i]+np.cos(b))
        d = np.append(d,np.sqrt( x[i]**2  + y[i]**2 + z[i]**2))
        i=i+1
    numbers[j]=i
    print j


plt.hist(numbers)
plt.xlabel("Pasos")
plt.ylabel("Fotones")
plt.title ("Central")
plt.savefig('histo_difusion_solar_central_'+str(n_photons)+'.pdf')
