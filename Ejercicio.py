#funciones 
def vol_pircuadrada():
    print ("Ingresa")
    altura=int(input("valor de la altura: "))
    lado_base=int(input("valor de un lado de la base: "))
    areab=lado_base*lado_base
    vol=(areab*altura)/3
    print ("El volumen es ",vol," cm3")

import math
def funcion():
    r=float(input("Ingrese el radio de la esfera : "))
    print("Radio: ",r , "m")
    v=4/3*math.pi*pow(r,3)

    print("El volumen de la esfera es: ", "%1.2f" %v , "m3")

def Funcion2() :
    a=float(input("Ingrese el valor de a del lado rectangular: "))
    b=float(input("Ingrese el valor de b del lado rectangular: "))
    h=float(input("Ingrese la altura de la piramide rectangular: "))

    v=(a*b*h)/3

    print("El volumen de la piramide con base rectangular es: ", "%1.2f"%v, "m3")
    
def vol_cubo():
    print ("Ingrese el valor del lado para el cubo")
    lado=int(input("valor:")
    volumen=lado*lado*lado
    print("\nEl volumen del cubo es: ",volumen)


#codigo
var=1
op=0
while (var!=0):
    print ("\t Menu")
    print("1: Cubo","\n2: Piramide de Base Triangular","\n3: Piramide de Base Cuadrada","\n4: Esfera","\n5: SALIR")
    op=int(input("Escoja una opcion: "))
    if op==1:            
        print("Seleccionaste Cubo")
        vol_cubo()
        var=0
    elif op==2:
        print("Seleccionaste Piramide de base triangular")
        Funcion2()
        var=0
    elif op==3:
        print("Seleccionaste Piramide de base cuadrada")
        vol_pircuadrada()   
        var=0
    elif op==4:
        print("Seleccionaste Esferar")
        funcion()
        var=0
    elif op==5:
        print ("GRACIAS")
        var=0
    else:
        print("\t Error")


    
