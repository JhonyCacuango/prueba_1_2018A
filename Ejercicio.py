#funciones 
def vol_pircuadrada():
    print ("Ingresa")
    altura=int(input("valor de la altura: "))
    lado_base=int(input("valor de un lado de la base: "))
    areab=lado_base*lado_base
    vol=(areab*altura)/3
    print ("El volumen es ",vol," cm3")
#codigo
var=1
op=0
while (var!=0):
    print ("\t Menu")
    print("1: Cubo","\n2: Piramide de Base Triangular","\n3: Piramide de Base Cuadrada","\n4: Esfera","\n5: SALIR")
    op=int(input("Escoja una opcion: "))
    if op==1:            
        print("Seleccionaste Cubo")
        var=0
    elif op==2:
        print("Seleccionaste Piramide de base triangular")
            
        var=0
    elif op==3:
        print("Seleccionaste Piramide de base cuadrada")
        vol_pircuadrada()   
        var=0
    elif op==4:
        print("Seleccionaste Esferar")
        
        var=0
    elif op==5:
        print ("GRACIAS")
        var=0
    else:
        print("\t Error")


    