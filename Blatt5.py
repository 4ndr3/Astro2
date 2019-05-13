#Bibliotheken imprtieren
import os
os.system('clear')	#Bildschrim leeren Unixoiden
#os.system('cls')	#Bildschrim leeren Windows

import numpy as np
import matplotlib.pyplot as plt

#Konstanten importieren
from scipy.constants import G
print(G)
from scipy.constants import pi
from astropy.constants import M_sun
print(M_sun.value)
from astropy.constants import M_jup
print(M_jup.value)
from astropy.constants import au
print (au.value)

#Daten setzen in SI
Exoplanet_Name = ['CoRoT-3 b','Kepler-14 b','Kepler-186 f','Kepler-440 b','HD 141399 d','HD 188015 b','HD 285507 b','WASP-114 b']
Exoplanet_Periode_inTagen = np.array([4.257, 6.790, 129.946, 101.111, 1070, 461, 6.088, 1.549])
Exoplanet_Periode = Exoplanet_Periode_inTagen * 86400 #Konvertiert in [s]
Exoplanet_Masse_inJupitermassen = np.array([22, 8.4, 0.0042, 0.0137, 1.19, 1.47, 0.92, 1.77])
Exoplanet_Masse =  Exoplanet_Masse_inJupitermassen * M_jup.value #Jupitermassen konvertiert in [Kg]
Expolanet_Muttersternmasse_inSonnenmassen = np.array([1.37, 1.51, 0.48, 0.58, 1.07, 1.06, 0.73, 1.29])
Expolanet_Muttersternmasse = Expolanet_Muttersternmasse_inSonnenmassen * M_sun.value #Sonnenmassen konvertiert in [Kg]


#a) Große Halbachsen berechnen
M = Exoplanet_Masse + Expolanet_Muttersternmasse
a = ((Exoplanet_Periode**2 * G * M) / (4 * pi**2)) ** (1/3)
a_inAU = a / au.value

#Ausgabe
#-------


#Gegeben
print('Gegeben')
print('=======')
print('Name		Perioden [d]	Masse [m_Jupiter]	Muttersternmasse [m_Sonne]')
for Zeile in zip(Exoplanet_Name, Exoplanet_Periode_inTagen, Exoplanet_Masse_inJupitermassen, Expolanet_Muttersternmasse_inSonnenmassen):
    print(Zeile[0],"	{1:3.2f}		{2:3.3f}			{3:3.3f}".format(Zeile[0], Zeile[1], Zeile[2], Zeile[3]))
print('\n')
print('\n')

#a)
print('a) Gesucht: Große Halbachsen a')
print('==============================')
print('Name		M [10^30 Kg]	a [Km]		a [AU]')
for Zeile in zip(Exoplanet_Name, M, a, a_inAU):
    print(Zeile[0],"	{1:3.3f}		{2:3.0f}		{3:3.3f}".format(Zeile[0], Zeile[1]/1e30, Zeile[2]/1000, Zeile[3]))

#b)

plt.plot(a_inAU, Exoplanet_Periode_inTagen)
#Abszisse formatieren
plt.xscale('log')
plt.xlabel("$a$ [AU]")

#Ordniate formatiern
plt.yscale('log')
plt.ylabel("$P$ [d]")

plt.show()
print('b) Gesucht: Umlaufzeit über große Halbachse')
print('===========================================')
print('s. Plot. Keine gerade Linie wegen Messungenauigkeiten.')

#c)
print('a) Gesucht: Große Halbachsen a')
print('==============================')
print('Name		M [10^30 Kg]	a [Km]		a [AU]')

