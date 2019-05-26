import random
lista_de_palabras=['hector','mike','david','emaotaku','alejandro','rafa','fili','ema'] #Lista de palabras
#Los nombres de los pedejos de mi salon. XD
letraparaadivinar=random.choice(lista_de_palabras)#Palabra al azar
letraingresada=""
vidas=5

print("Este es el juego del Ahorcado")
nombre=input("Ingresa tu nombre: ")
print("Hola "+nombre," Vamos a jugar")
print("Comienza a adivinar")
while vidas > 0:
    fallas=0
    for letra in letraparaadivinar:
        if letra in letraingresada:
            print(letra,end=" ")
        else:
            print("_  ",end=" ")
            fallas+=1
    if fallas==0:
        print(F" Felicidades {nombre} , te fue bien")
        break
    ingreso_letra=input(" Introduce una letra:  ")
    letraingresada+=ingreso_letra
    if ingreso_letra not in letraparaadivinar:
        vidas-=1
        print(F"Te has equivocado {nombre}")
        print(F"{nombre} tienes {vidas} vidas")      
    if vidas==0:
        print(F"Lo siento {nombre} Perdiste")
        print(F"Palabra correcta {letraparaadivinar[:]}")

    

     




