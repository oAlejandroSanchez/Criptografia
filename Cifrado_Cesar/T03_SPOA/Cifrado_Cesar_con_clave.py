# Universidad Nacional Autónoma de México
# Facultad de Ingeniería

# Asignatura: Criptografía
# Nombre: Alejandro Pérez

# Ejercicio 2:
# Algoritmo César con clave. Cifrar y descifrar el
# lema de la UNAM, con clave. (sus dos apellidos)

# Importamos el alfabeto
import string

# Apellidos del usuario
apellidos = ""

# Alfabeto 
alfabeto = alfabeto_orig = string.ascii_uppercase

# Mensaje
mensaje = ''
# Mensaje cifrado
encrypt = ''
# Mensaje descifrado
desencrypt = ''

# Revisamos si la letra se encuentra dentro de los apellidos
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
        print(" *** Revisa tus apellidos *** \n")
    
    # Se imprime en pantalla el alfabeto completo
    alfabeto = aux
    for letra in alfabeto:
        print("| " + letra + " | " + str(alfabeto.find(letra)) + 
              (" ","  ")[alfabeto.find(letra) < 10] + "| ")
    
# Se cifra el mensaje
def encryptMessage():
    global mensaje,encrypt,alfabeto,alfabeto_orig
    
    for letra in mensaje:
        if letra != ' ':
            encrypt += alfabeto[alfabeto_orig.find(letra)]
        else:
            encrypt += letra

    print("El mensaje cifrado es: " + encrypt)
    
# Se descifra el mensaje
def desencryptMessage():
    global desencrypt,alfabeto_orig,encrypt
    
    for letra in encrypt:
        if letra != ' ':
            desencrypt += alfabeto_orig[alfabeto.find(letra)]
        else:
            desencrypt += letra
    
    print("El mensaje descifrado es: " + desencrypt)
    
    
# Funcion principal
def main():
    global apellidos,mensaje
    
    # Título del algoritmo
    print("\t\tAlgoritmo Cesar con clave\n")
    
    # Se ingresan los apellidos del usuario
    apellidos = input("Escribe tus apellidos sin separación: ")
    apellidos = apellidos.upper()
    
    # Se determina el alfabeto
    alphabet()
    print("")
    
    # Se obtiene el mensaje
    mensaje = input("Escribe el mensaje a cifrar: ")
    mensaje = mensaje.upper()
    
    # Se cifra el mensaje
    encryptMessage()
    
    # Se descifra el mensaje
    desencryptMessage()

# Se ejecuta el programa a través de la función principal
main()
