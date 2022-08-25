'''
numero=5

while(numero<10):
    
    print("Mensaje dentro de la cuerda")
    numero+=1
else: 
    print("Byeeeeeeeeeeeeeee")

print("Mensaje fuera de la cuerda")
'''

opcion=1
print("*****Menu******")
print("1.SUMA")
print("2.RESTA")
print("0.SALIR")

while(opcion != 0):

    opcion=int(input("Digite una opcion: ")) 

    if(opcion == 1):
        print("Sumando")
    elif(opcion == 2):
        print("Restando")
    elif(opcion == 0):
        break
    else:
        print("Digite una opcion valida")