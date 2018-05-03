# -*- coding: utf-8 -*-
"""
Created on Thu May  3 09:49:13 2018

@author: ESFOT
"""

codificador=["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]
codificador1=[1,2,3,4,5,6,7,8,9,10,11,12,13,13,15,16,17,18,19,20,21,22]
for p in codificador:
    print (p,len(p))
    
a=codificador[0]+codificador[1]+codificador[3]+codificador[11]+codificador[3]+codificador[13]+codificador[3]
b="013113133"
print(b)
print (a)

archivo_ca=(open('C:/Users/ESFOT/Documents/prueba/4.txt','w'))
archivo_ca.write(b+"\n")
archivo_ca.write(a)
archivo_ca.close

