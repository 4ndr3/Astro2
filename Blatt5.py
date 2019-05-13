#Bibliotheken imprtieren
import os
os.system('clear')	#Bildschrim leeren Unixoiden
#os.system('cls')	#Bildschrim leeren Windows

import numpy as np
import matplotlib.pyplot as plt

#Konstanten importieren
from scipy.constants import G
from scipy.constants import pi
from astropy.constants import M_sun
from astropy.constants import M_jup
from astropy.constants import au

#Daten setzen
Exoplanet_Name = ['CoRoT-3 b','Kepler-14 b','Kepler-186 f','Kepler-440 b','HD 141399 d','HD 188015 b','HD 285507 b','WASP-114 b']
Exoplanet_Periode_inTagen = np.array([4.257, 6.790, 129.946, 101.111, 1070, 461, 6.088, 1.549])
Exoplanet_Masse_inJupitermassen = np.array([22, 8.4, 0.0042, 0.0137, 1.19, 1.47, 0.92, 1.77])
Expolanet_Muttersternmasse_inSonnenmassen = np.array([1.37, 1.51, 0.48, 0.58, 1.07, 1.06, 0.73, 1.29])
Exoplanet_Klasse = ['CoRoT-3 b','Kepler-14 b','Kepler-186 f','Kepler-440 b','HD 141399 d','HD 188015 b','HD 285507 b','WASP-114 b']

#Daten nach SI konvertieren
Exoplanet_Periode = Exoplanet_Periode_inTagen * 86400 # [s]
Exoplanet_Masse =  Exoplanet_Masse_inJupitermassen * M_jup.value # [Kg]
Expolanet_Muttersternmasse = Expolanet_Muttersternmasse_inSonnenmassen * M_sun.value # [Kg]


#Gegeben
#=======
print('Gegeben')
print('=======')
print('Name		Perioden [d]	Masse [m_Jupiter]	Muttersternmasse [m_Sonne]')
print('-----------------------------------------------------------------------')
for Zeile in zip(Exoplanet_Name, Exoplanet_Periode_inTagen, Exoplanet_Masse_inJupitermassen, Expolanet_Muttersternmasse_inSonnenmassen):
    print(Zeile[0],"	{1:3.2f}		{2:3.3f}			{3:3.3f}".format(Zeile[0], Zeile[1], Zeile[2], Zeile[3]))
print('\n')


#Ergebnisse
#==========
#a)
M = Exoplanet_Masse + Expolanet_Muttersternmasse
a = ((Exoplanet_Periode**2 * G * M) / (4 * pi**2)) ** (1/3)
a_inAU = a / au.value

print('a) Gesucht: Große Halbachsen a')
print('==============================')
print('Name		M [10^30 Kg]	a [Km]		a [AU]')
print('-------------------------------------------')
for Zeile in zip(Exoplanet_Name, M, a, a_inAU):
    print(Zeile[0],"	{1:3.3f}		{2:3.0f}		{3:3.3f}".format(Zeile[0], Zeile[1]/1e30, Zeile[2]/1000, Zeile[3]))


#b)
plt.plot(a_inAU, Exoplanet_Periode_inTagen, 'ro')
#Abszisse formatieren
plt.xscale('log')
plt.xlabel("$a$ [AU]")

#Ordniate formatiern
plt.yscale('log')
plt.ylabel("$P$ [d]")

print('')
print('b) Gesucht: Umlaufzeit über große Halbachse')
print('===========================================')
print('s. Plot. Keine gerade Linie wegen Messungenauigkeiten.')


#c)
for i in range(Exoplanet_Masse_inJupitermassen.size):
	if Exoplanet_Masse_inJupitermassen[i] >=13.:
		Exoplanet_Klasse[i] = 'Brauner Zwerg (Masse >= 13 m_Jupiter)'
	elif Exoplanet_Masse_inJupitermassen[i] >=.1:
		Exoplanet_Klasse[i] = 'Jupiterähnlicher Planet (Masse zwischen .1 und 13 m_Jupiter)'
		if Exoplanet_Periode_inTagen[i] <= 5.:
			Exoplanet_Klasse[i] = 'Heißer Jupiter (Umlaufzeit <= 5 Tage)'
	else:
		Exoplanet_Klasse[i] ='Erdähnlicher Planet (Mangels anderer Daten: keine der anderen Klassen)'
	
		
print('')
print('c) Gesucht: Klassifizierung der Objekte')
print('=======================================')
print('Name		 Klasse')
print('----------------')
for Zeile in zip(Exoplanet_Name, Exoplanet_Klasse):
	print (Zeile[0],"	",Zeile[1])
	
plt.show() #für b)
