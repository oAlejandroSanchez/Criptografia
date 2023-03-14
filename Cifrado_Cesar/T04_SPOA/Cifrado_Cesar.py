# Universidad Nacional Autónoma de México
# Facultad de Ingeniería

# Nombre: Sánchez Pérez Omar Alejandro
# No. Cuenta: 315072264

# Asignatura: Criptografía
# Semestre: 2023 - 2

# Ejercicio 1: Programar el algoritmo de César, Cifrar y Descifrar para...
# a) k = 3
# b) Con clave, completando el abecedario
# c) Con clave única del mismo tamaño que el mensaje

# Abecedario
alfabeto = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
nuevo_alfabeto = ''

# Clave
clave = ''

# Mensaje
mensaje = ''

# Revisamos si la letra se encuentra dentro de los apellidos
def is_exist(letra):
    global clave
    return letra in clave

# Imprimimos en pantalla el alfabeto
def printAlphabet(alfabeto):
    print(alfabeto)
    for letra in alfabeto:
        print("\t| " + letra + " | " + str(alfabeto.find(letra)) + (" ","  ")[alfabeto.find(letra) < 10] + "|" )

# Definimos el alfabeto
def alphabet(opcion):
    global alfabeto, clave, nuevo_alfabeto, mensaje
    aux = ''

    if opcion == 'a':
        printAlphabet(alfabeto)
    elif opcion == 'b':
        clave = input("\tEscribe la clave: ").upper()
        if clave.isalpha():
            for letra in clave:
                if letra not in aux:
                    aux += letra
                    
            for letra in alfabeto:
                if not is_exist(letra):
                    aux += letra
        
            nuevo_alfabeto = aux
            printAlphabet(aux) 
        else:
            print("\t\t*** Revisa la clave que ingresaste *** \n")

    elif opcion == 'c':
        clave = mensaje
                
        for letra in clave:
            if letra != ' ' and letra not in aux:
                aux += letra
    
        nuevo_alfabeto = aux
        printAlphabet(aux) 

# Obtenemos el mensaje
def getMessage():
    global mensaje
    mensaje = input("\tEscribe el mensaje a cifrar: ").upper()

def Encrypt_and_Decrypt(mensaje,position,key,aux,state):
    global alfabeto

    for letra in mensaje:
        if letra != ' ':
            position = (alfabeto.find(letra) + key) % len(alfabeto)
            aux += alfabeto[position]
            # Se imprime el procedimiento de encriptado del mensaje 
            print("\t("+ str(alfabeto.find(letra)) +("","+")[state]+ str(key) +") mod ("+ str(len(mensaje)) +") = "+ str(position))
        else:
            aux += ' '
            print("")
    
    return(aux)

# Clave K
def clave_K(key):
    global mensaje

    # Encriptando el mensaje
    # Instrucciones
    print("\tPara encriptar el mensaje, se puede usar la siguiente ecuación: ")
    print("\tE = (posición de la letra + K) mod (tamaño del alfabeto) \n")
    encrypt = ''
    encrypt = Encrypt_and_Decrypt(mensaje,0,key,'',True)
    print("\t\tMensaje cifrado: " + encrypt + "\n")

    # Descifrando el mensaje
    # Instrucciones
    print("\tPara descifrar el mensaje, se reemplaza la suma por una resta")
    print("\tD = (posición de la letra - K) mod (tamaño del alfabeto) \n")
    desencrypt = ''
    desencrypt = Encrypt_and_Decrypt(encrypt,0,(-1)*key,'',False)
    print("\t\tMensaje descifrado: " + desencrypt +"\n\n")

# Con clave reemplazando elementos del alfabeto
def con_Reemplazo(alfabeto):
    # Encriptando el mensaje
    global mensaje,nuevo_alfabeto
    
    # Mensaje cifrado
    encrypt = ''

    for letra in mensaje:
        if letra != ' ':
            encrypt += nuevo_alfabeto[alfabeto.find(letra)]
        else:
            encrypt += letra
    
    print("\tEl mensaje cifrado es: " + encrypt)

    # Descifrando el mensaje
    # Mensaje descifrado
    desencrypt = ''

    for letra in encrypt:
        if letra != ' ':
            desencrypt += alfabeto[nuevo_alfabeto.find(letra)]
        else:
            desencrypt += letra
    
    print("\tEl mensaje descifrado es: " + desencrypt)

# Función principal
def main():
    global alfabeto, nuevo_alfabeto

    # Se crea un menú, por lo tanto esta operación
    opcion = ''

    # Título
    print("\n\n\t\tCifrado César (Ejercicio 1)\n")

    # Menu
    print("\tElige una opción:")
    print("\ta) K = 3")
    print("\tb) Con clave, completando el abecedario")
    print("\tc) Con clave única del mismo tamaño que el mensaje\n")

    opcion = input("\tOpción: ").lower()

    if opcion == 'a':
        getMessage()
        print("\tTamaño de la clave  K = 3")
        alphabet(opcion)
        clave_K(3)
    elif opcion == 'b':
        getMessage()
        alphabet(opcion)
        con_Reemplazo(alfabeto)
    elif opcion == 'c':
        getMessage()
        alphabet(opcion)
        con_Reemplazo(nuevo_alfabeto)
    else:
        print("\t\t\nOpción inválida\n")

# Ejecutamos la función principal
main()

