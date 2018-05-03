# -*- coding: utf-8 -*-
"""
Created on Thu May  3 08:26:16 2018

@author: ESFOT
"""


from io import open
print ("Numeros binarios a decimales")
archivo1=open('C:/Users/ESFOT/Documents/prueba/1.txt','r')
num=archivo1.readline()
print(num)
a=2*2*2*2*2
b=2*2*2
c=0
d=0
e=1
res=a+b+c+d+e
print(res)
archivo1.close()
    


print ("Guardar en otro ducumento")
archivo2=open('C:/Users/ESFOT/Documents/prueba/2.txt','w')
archivo2.write("Jhony Javier Cacuango...")
archivo2.write(res)
archivo2.close()



