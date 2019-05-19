#Bibliotheken imprtieren
import os
os.system('clear')	#Bildschrim leeren Unixoiden
#os.system('cls')	#Bildschrim leeren Windows

import numpy as np
import matplotlib.pyplot as plt

#Konstanten importieren
from scipy.constants import pi
from scipy.constants import h
from scipy.constants import m_e
from scipy.constants import k
from scipy.constants import u
#from scipy.constants import G
from astropy.constants import au
from astropy.constants import M_sun
#from astropy.constants import M_jup

#a) 
A = 4. # Massenzahl He
Z = 2. # Ordnungszahl He
Koeffizient = h**2. / (20. * m_e * k) * (3. / (pi * A * u))**(2./3) * Z**(5./3) / (Z+1.)

print('a) Koeffizient für He:',Koeffizient,'K * m^3 / Kg')

#b)
def Mindestdichte(T_krit):
	return (T_krit / Koeffizient) ** (3. / 2)


T_krit = np.logspace(4.0, 9.0, num=21, endpoint=True)
plt.plot(T_krit, Mindestdichte(T_krit), 'ro') # ro = rote Kreise


#Abszisse formatieren
plt.xscale('log')
plt.xlabel("$Tkrit$ [K]")

#Ordniate formatiern
plt.yscale('log')
plt.ylabel("$Mindestdichte$ [Kg/m^3]")

plt.show() 

#c)
T_OStern = 3e4 # [K]
T_weisserZwerg = 1e7 # [K]
T_HeliumBlitz = 1e8 # [K]
M_HeliumBlitz = 2 * M_sun.value # [Kg]

