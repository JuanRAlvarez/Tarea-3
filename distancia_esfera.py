import numpy as np
import sys

lat1 = float(sys.argv[1])
lon1 = float(sys.argv[2])
lat2 = float(sys.argv[3])
lon2 = float(sys.argv[4])

lat1 = lat1*np.pi/180
lon1 = lon1*np.pi/180
lat2 = lat2*np.pi/180
lon2 = lon2*np.pi/180

dlat=lat1-lat2
dlat = dlat/2
dlon=lon1-lon2
dlon = dlon/2

earthr = 6371

sinsqa = (np.sin(dlat))**2
sinsqb = (np.sin(dlon))**2

hav = 2*earthr * np.arcsin(np.sqrt((sinsqa)+(np.cos(lat1)*np.cos(lat2)*(sinsqb))))

print "La distancia entre los dos puntos es de", hav, "km"
