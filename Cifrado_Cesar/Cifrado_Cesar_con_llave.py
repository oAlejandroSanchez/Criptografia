# Universidad Nacional Autónoma de México
# Facultad de Ingeniería

# Asignatura: Criptografía
# Nombre: Alejandro Pérez

# Ejercicio 1:
# Algoritmo César. Cifrar y descifrar el lema de la UNAM, con su letra asignada, 
# (SEGUNDA consonante de su nombre).

# Importamos el alfabeto
import string

# Vocales
vocales = "AEIOU"

# Nombre el usuario
nombre = ""
# Segunda consonante del nombre
consonante = ''

# Alfabeto
alfabeto = string.ascii_uppercase

# Mensaje
mensaje = ''
# Mensaje cifrado
encrypt = ''
# Mensaje descifrado
desencrypt = ''

# Determinamos si e una vocal
def is_vocal(letra):
    global vocales
    return letra in vocales

# Encontramos la segunda consonante del nombre dado
def second_consonant():
    global nombre, consonante
    contador = 0
    
    if nombre.isalpha():
        for letra in nombre:
            if not is_vocal(letra):
                print(contador)
                contador += 1;
                consonante = letra
            elif contador == 2:
                break;
    else:
        print(" *** Revisa que tu nombre solo contenga letras *** ")

# Definimos el alfabeto
def alphabet():
    global nombre,consonante,alfabeto
    
    for letra in alfabeto:
        print("| " + letra + " | " + str(alfabeto.find(letra)) + 
              (" ","  ")[alfabeto.find(letra) < 10] + "|" + 
              ("", "<--- Esta es la consonante que se ocupará")[letra == consonante])
            

# Cifrando el mensaje
def encryptMessage():
    global mensaje,alfabeto,encrypt
    
    # Posicion del cifrado
    position = 0
    
    # Instrucciones
    print("Para encriptar el mensaje, se puede usar la siguiente ecuación: ")
    print("E = (posición de la letra + llave) mod (tamaño del alfabeto) \n")
    
    for letra in mensaje:
        if letra != ' ':
            position = (alfabeto.find(letra) + (alfabeto.find(consonante)+1)) % len(alfabeto)
            encrypt += alfabeto[position]
            print("(" + str(alfabeto.find(letra)) + " + " + str(alfabeto.find(consonante) + 1) 
              + ") mod " + str(len(alfabeto)) + " = " + 
              str(position))
        else:
            encrypt += ' '
            print("")
                    
    print("\nMensaje cifrado: " + encrypt + "\n")
    
# Se descifra el mensaje
def desencryptMessage():
    global mensaje,alfabeto,desencrypt
    
    # Posicion 
    position = 0
    
    # Instrucciones
    print("Para descifrar el mensaje, se reemplaza la suma por una resta")
    print("D = (posición de la letra - llave) mod (tamaño del alfabeto) \n")
    
    for letra in encrypt:
        if letra != ' ':
            position = (alfabeto.find(letra) - (alfabeto.find(consonante)+1)) % len(alfabeto)
            desencrypt += alfabeto[position]
            print("(" + str(alfabeto.find(letra)) + " - " + str(alfabeto.find(consonante) + 1) 
              + ") mod " + str(len(alfabeto)) + " = " + 
              str(position))
        else:
            desencrypt += ' '
            print("")
                    
    print("\nMensaje descifrado: " + desencrypt)
    
              
# Función principal
def main():
    global nombre, mensaje
    
    # Título del algoritmo
    print("\t\t\tAlgoritmo Cesar (Sustitución)\n")
    
    # Se ingresa el nombre del usuario
    nombre = input("Ingresa tu nombre: ")
    nombre = nombre.upper()
    second_consonant()
    
    # Se imprime el mensaje y se indica la letra y posición que se ocupará
    print("El alfabeto es: ")
    alphabet()
    
    # Se solicita el mensaje
    mensaje = input("\nEscribe el mensaje a cifrar: ")
    mensaje = mensaje.upper()
    
    # Se cifra el mensaje
    encryptMessage()
    
    # Se descifra el mensaje
    desencryptMessage()
    
# Se ejecuta la función principal
main()
