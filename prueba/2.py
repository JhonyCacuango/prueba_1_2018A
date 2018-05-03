# -*- coding: utf-8 -*-
"""
Created on Thu May  3 08:59:30 2018

@author: ESFOT
"""
from io import open

cadena=["Python","es","un","lenguaje","de","programacion","avanzada"]

i=cadena[0]
a=cadena[1]
b=cadena[2]
c=cadena[3]
d=cadena[4]
e=cadena[5]
f=cadena[6]
res=f+" "+e+" "+d+" "+c+" "+b+" "+a+" "+i
print (res)
archivo_ca=(open('C:/Users/ESFOT/Documents/prueba/3.txt','w'))
archivo_ca.write(res)
archivo_ca.close



