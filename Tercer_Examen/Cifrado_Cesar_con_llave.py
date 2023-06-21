# Universidad Nacional Autónoma de México
# Facultad de Ingeniería

# Asignatura: Criptografía
# Nombre: Alejandro Pérez

# Ejercicio 1: Algoritmo Cesar

# Nombre el usuario
nombre = ""
# llave
llave = 0

# Alfabeto
alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

# Mensaje
mensaje = ''
# Mensaje cifrado
encrypt = ''
# Mensaje descifrado
desencrypt = ''

# Definimos el alfabeto
# def alphabet():
#     global nombre,consonante,alfabeto
    
#     for letra in alfabeto:
#         print("| " + letra + " | " + str(alfabeto.find(letra)) + 
#                 (" ","  ")[alfabeto.find(letra) < 10] + "|")

def is_exist(letra):
    global apellidos
    return letra in apellidos
     
# Definimos el alfabeto
def alphabet():
    global apellidos,alfabeto
    
    # Variable auxiliar
    aux = ''
    
    if apellidos.isalpha():
        for letra in apellidos:
            if letra not in aux:
                aux += letra
                
        for letra in alfabeto:
            if not is_exist(letra):
                aux += letra
    else:
        print(" *** Revisa la palabra clave *** \n")
    
    # Se imprime en pantalla el alfabeto completo
    alfabeto = aux
    for letra in alfabeto:
        print("| " + letra + " | " + str(alfabeto.find(letra)) + 
              (" ","  ")[alfabeto.find(letra) < 10] + "| ")

# Cifrando el mensaje
def encryptMessage(llave):
    global mensaje,alfabeto,encrypt
    
    # Posicion del cifrado
    position = 0
    
    # Instrucciones
    print("Para encriptar el mensaje, se puede usar la siguiente ecuación: ")
    print("E = (posición de la letra + llave) mod (tamaño del alfabeto) \n")
    
    for letra in mensaje:
        if letra != ' ':
            position = (alfabeto.find(letra) + (llave)) % len(alfabeto)
            encrypt += alfabeto[position]
            print("(" + str(alfabeto.find(letra)) + " + " + str(llave) 
              + ") mod " + str(len(alfabeto)) + " = " + 
              str(position))
        else:
            encrypt += ' '
            print("")
                    
    print("\nMensaje cifrado: " + encrypt + "\n")
    
# Se descifra el mensaje
def desencryptMessage(llave):
    global mensaje,alfabeto,desencrypt
    
    # Posicion 
    position = 0
    
    # Instrucciones
    print("Para descifrar el mensaje, se reemplaza la suma por una resta")
    print("D = (posición de la letra - llave) mod (tamaño del alfabeto) \n")
    
    for letra in encrypt:
        if letra != ' ':
            position = (alfabeto.find(letra) - (llave)) % len(alfabeto)
            desencrypt += alfabeto[position]
            print("(" + str(alfabeto.find(letra)) + " - " + str(llave) 
              + ") mod " + str(len(alfabeto)) + " = " + 
              str(position))
        else:
            desencrypt += ' '
            print("")
                    
    print("\nMensaje descifrado: " + desencrypt)
    
              
# Función principal
def main():
    global nombre, mensaje, llave
    
    # Título del algoritmo
    print("\t\t\tAlgoritmo Cesar (Sustitución)\n")
    
    # Se imprime el mensaje y se indica la letra y posición que se ocupará
    print("El alfabeto es: ")
    alphabet()
    
    # Se solicita el mensaje
    mensaje = input("\nEscribe el mensaje a cifrar: ")
    mensaje = mensaje.upper()

    llave = int(input("Ingresa la llave: "))
    
    # Se cifra el mensaje
    encryptMessage(llave)
    
    # Se descifra el mensaje
    desencryptMessage(llave)
    
# Se ejecuta la función principal
main()
