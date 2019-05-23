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


T_krit = np.logspace(4.0, 9.0, num=11, endpoint=True)
plt.plot(T_krit, Mindestdichte(T_krit)) # ro = rote Kreise


#Abszisse formatieren
plt.xscale('log')
plt.xlabel("$Tkrit$ [K]")
plt.xlim([1,1e9])


#Ordniate formatiern
plt.yscale('log')
plt.ylabel("$Mindestdichte$ [Kg/m^3]")
#plt.ylim([1,1e10])

print('')
print('b) Gesucht: Mindestdichte Entartung')
print('======================================')
print('s. Plot.')


#c)
Objekt_Name = ['O-Stern','Weißer Zwerg','Helium-Blitz']
Objekt_T = np.array([3e4, 1e7, 1e8]) # [K]
Objekt_m = np.array([60 * M_sun.value, 0, 2 * M_sun.value]) # [Kg], dummy-Wert für weissen Zwerg
weisserZwerg_ro = 1e9 # [Kg / cm^3]
Objekt_ro_min = [''] * Objekt_T.size
Objekt_ro = np.array([1, 1, 1]) # [Kg/m^3], dummy Dichten, weil woher nehmen?
Objekt_Entartung = [''] * Objekt_T.size

for i in range(Objekt_T.size):
	Objekt_ro_min[i] = Mindestdichte(Objekt_T[i])

for i in range(Objekt_ro.size):
	if 	Objekt_ro[i] < Objekt_ro_min[i]:
		Objekt_Entartung[i] = True

print('')
print('c) Gesucht: Entartung')
print('======================================')
print('Objekt		T [10^3 K]	ro_min [Kg/m^3]	ro [Kg/m^3]	Entartung')
print('-----------------------------------------------------------------------------')
for Zeile in zip(Objekt_Name, Objekt_T, Objekt_ro_min, Objekt_ro, Objekt_Entartung):
    print(Zeile[0],"	{1:1.0f}		{2:1.0f}		{3:1.0f}".format(Zeile[0], Zeile[1]/1000, Zeile[2], Zeile[3]),Zeile[4])

print('')
print('Ergebnis ist Prinzipdarstellung des Codes. Es ist falsch weil unklar ist wo die Objektdichte herkommen soll.')

plt.show() # für b)
