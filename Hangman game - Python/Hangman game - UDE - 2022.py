#Proyecto fin de curso - “Programación Python” UDE - 2022

#EL AHORCADO

#Matías Tournier - Adrián Parrilla - Francisco del Rio

import random

#Lista que contiene los dibujos del ahorcado en todas sus etapas.
ahorcado = ["""
     +----+
     |    |
     |
     |
     |
     |
    ========""","""
     +----+
     |    |
     |    O
     |
     |
     |
    ========""","""
     +----+
     |    |
     |    O
     |    |
     |
     |
    ========""","""
     +----+
     |    |
     |    O
     |   /|
     |
     |
    ========""","""
     +----+
     |    |
     |    O
     |   /|\ 
     |
     |
    ========""","""
     +----+
     |    |
     |    O
     |   /|\ 
     |   /
     |
    ========""","""
     +----+
     |    |
     |    O
     |   /|\ 
     |   / \ 
     |
    ========"""]

#Lista que contiene las palabras a ser adivinadas por el jugador.
diccionario = ["curso","python","computadora","programa","juego","grupo","estudio","heladera","castaña","fortaleza","migraña","aspirina"]

#Cadena de texto con todas las letras del abecedario.
abecedario = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

#Contador de intentos/vidas del jugador, se tendrá 6 vidas.
contadorVidas = 0

#Con random, se selecciona una palabra aleatoria del "diccionario" y se almacena en la variable.
palabraRandom = random.choice(diccionario)
palabraRandom = palabraRandom.upper()

#Crea una lista con la palabra seleccionada, cada valor de la lista es una de las letras.
listaLetras = list(palabraRandom)

#Almacena el int() de la longitud de la palabra que se eligió aleatoriamente.
largoPalabra = len(listaLetras)

#Lista de guiones bajos [_, _, _, ...] con el largo de la palabra aleatoria.
palabraOculta = ["_" for _ in range(largoPalabra)] 

#FUNCIONES
def ingreseLetra(intento):
    #Devuelve la letra que el jugador ingresó y filtra que se ingrese una letra y no otra cosa.
    while True:
        letra = input("\nIngrese una letra: ")
        letra = letra.upper()
        if letra == palabraRandom:
            print("\nHAS GANADO!\n")
            exit()
        #elif len(letra) > 2 and letra != palabraRandom:
            #print("palabra incorrecta")
            #contador += 1
            #break
        elif len(letra) != 1:
            print ("\nERROR: Ingresa una sola letra.") 
        elif letra in intento:
            print ("\nERROR: Ya has ingresado esa letra, intenta nuevamente.")
        elif letra not in abecedario:
            print ("\nERROR: Tiene que ser una letra.")
        else:
            return letra

def imprimir(palabra):
    #Pequeña función de impresión y salto de línea.
    print("\nLETRAS:  "," ".join(palabra))

print("\n======= A H O R C A D O =======")

imprimir(palabraOculta)
intento = "" #Cadena de texto que contendrá las letras utilizadas
contador = 0
ganador = False
while contadorVidas < 6: #Son 6 intentos por las 6 partes del cuerpo. Comienza solo la "piola".
    print(ahorcado[contadorVidas]) #Imprimimos el tanteador inicial.
    letra = ingreseLetra(intento) #Utiliza la función para asegurarse que sea una letra y no repetida.
    intento += letra #Agrega la letra a los intentos ya ingresados
    acierto = False
    print("\n================================")
    for i in range(largoPalabra): #Recorre desde el indice 0 hasta la última letra de la palabra.
        if listaLetras[i] == letra: #Evalúa que la letra dada esté en la lista de la palabra aleatoria.
            palabraOculta[i] = letra #Reemplaza el guión bajo por la letra dada, modifica la lista.
            contador += 1 #Aumenta el contador, una letra de la palabra adivinada.
            acierto = True
    if not acierto: #Si la letra no está en la palabra, se pierde una vida.
        contadorVidas += 1 #Tendremos 6 vidas.
    imprimir(palabraOculta)
    if contador == largoPalabra: #Se adivinaron todas la letras
        ganador = True
        break   
if ganador:
    print("\nHAS GANADO!\n")
else:
    print(ahorcado[6]) #Imprime el último muñeco, el ahorcado final.
    print(f"\nHAS PERDIDO! \n\nLa palabra era: ",palabraRandom,"\n")



