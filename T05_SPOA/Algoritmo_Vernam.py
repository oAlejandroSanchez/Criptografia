# Universidad Nacional Autónoma de México
# Facultad de Ingeniería

# Asignatura: Criptografía
# Nombre: Alejandro Pérez

# Ejercicio 2: Programar el algoritmo de Vernam, cifrar y descifrar el mensaje
# "Fernando Casa Sola". Usando la clave Santiago (recuerden es en binario).

# Mensaje
mensaje = ''
mensaje_binario = []

# Clave
clave = ''
clave_binario = []

# Descifrado
descifrado_binario = []

# Convirtiendo en binario
def conversion_binario(numero):
    binario = ''

    while numero > 0:
        residuo = numero % 2
        binario = str(residuo) + binario
        numero = numero // 2
    
    return binario

# Determinamos el ASCII y el valor en binario del mensaje
def conversion_mensaje():
    global mensaje, mensaje_binario, clave

    while len(mensaje)%len(clave) != 0:
        mensaje += 'x'

    for letra in mensaje:
        mensaje_binario.append(conversion_binario(ord(letra)))

# Se determina el ASCII y el valor en binario de la clave
def conversion_clave():
    global clave, clave_binario
    
    for letra in clave:
        clave_binario.append(conversion_binario(ord(letra)))

# Cifrando el mensaje
def cifrado():
    global mensaje_binario, clave_binario, descifrado_binario
    aux = ''
    # temp1 = temp2 = False
    contador = 0

    for i in range(len(mensaje_binario)):
        if contador%len(clave_binario) == 0:
            contador = 0
        for j in range(len(mensaje_binario[i])):
            if mensaje_binario[i][j] == clave_binario[contador][j]:
                aux += '0'
            else:
                aux += '1'

        descifrado_binario.append(aux)
        contador += 1
        aux = ''
    
    print("\t\tEl mensaje en binario es: ", end='')
    for letra in mensaje_binario:
        print(letra, end='')

    print("\n\t\tEl mensaje cifrado quedó de la siguiente forma: ", end='')
    for letra in descifrado_binario:
        print(letra, end='')

# Descifrado
def descifrado():
    global descifrado_binario, clave_binario, mensaje_binario
    mensaje_binario = []
    contador = 0
    aux = ''

    for i in range(len(descifrado_binario)):
        if contador%len(clave_binario) == 0:
            contador = 0
        for j in range(len(descifrado_binario[i])):
            if descifrado_binario[i][j] == clave_binario[contador][j]:
                aux += '0'
            else:
                aux += '1'
        
        mensaje_binario.append(aux)
        contador += 1
        aux = ''

    print("\t\tEl mensaje descifrado en binario es: ", end='')
    for letra in mensaje_binario:
        print(letra, end='')
    
    print("\n\t\tEl mensaje descifrado es: ", end='')
    for letra in mensaje_binario:
        print(chr(int(letra, 2)), end='')

    print("\n\n")

# Función principal
def __main__():
    global mensaje, clave, mensaje_binario

    print("\t\tAlgoritmo de Vernam")
    mensaje = input("\n\t\tEscribe el mensaje a cifrar: ").strip()
    clave = input("\t\tEscribe la clave: ")

    conversion_mensaje()
    conversion_clave()

    print("\n\t\tCIFRANDO...\n")
    cifrado()

    print("\n\n\t\tDESCIFRANDO...\n")
    descifrado()

# Ejecutamos la función principal
__main__()
