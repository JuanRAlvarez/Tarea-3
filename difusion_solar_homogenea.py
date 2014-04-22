import numpy as np
import matplotlib.pyplot as plt
import sys

n_photons = int(sys.argv[1])
numbers = np.zeros(n_photons)
radius = 100

A = np.random.random(n_photons)
B = np.random.random(n_photons)
C = 2*B-1
R = 100
r = R*(np.random.random(n_photons))**(1/3.0)
theta = 2*np.pi*A
phi = np.arccos(C)

x0 = r * np.cos(theta) * np.sin(phi)
y0 = r * np.sin(theta) * np.sin(phi)
z0 = r * np.cos(phi)
d0 = np.sqrt(x0**2 + y0**2 + z0**2)

for j in range(n_photons):
    i=0
    x=np.empty((0))
    y=np.empty((0))
    z=np.empty((0))
    d=np.empty((0))

    x = np.append(x,x0[j])
    y = np.append(y,y0[j])
    z = np.append(z,z0[j])
    d = np.append(d,d0[j])

    while(d[i]<radius):

        a=np.pi*2*np.random.random()
        b=np.pi*np.random.random()
        x = np.append(x,x[i]+np.cos(a)*np.sin(b))
        y = np.append(y,y[i]+np.sin(a)*np.sin(b))
        z = np.append(z,z[i]+np.cos(b))
        d = np.append(d,np.sqrt( x[i]**2  + y[i]**2 + z[i]**2))
        i=i+1
    numbers[j]=i


plt.hist(numbers,bins=30)
plt.xlabel("Pasos antes de salir")
plt.ylabel("Fotones")
plt.title("Homogenea")
plt.savefig('histo_difusion_solar_homogenea_'+str(n_photons)+'.pdf')

