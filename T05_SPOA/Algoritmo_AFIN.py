# Universidad Nacional Autónoma de México
# Facultad de Ingeniería

# Asignatura: Criptografía
# Nombre: Alejandro Pérez

# Ejercicio 1:
# Programar el algoritmo AFIN C=x*M+b y descifrar el lema de la Universidad.
# Usando x=1, b=7 donde M es el mensaje.

# Alfabeto
alfabeto = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'

# Mensaje
mensaje = ''
M = 0
x = 1
b = 7

# Cifrado
cifrado_M = ''
C = 0

# Definimos el alfabeto
def alphabet():
    global alfabeto
    
    for letra in alfabeto:
        print("| " + letra + " | " + str(alfabeto.find(letra)) + 
              (" ","  ")[alfabeto.find(letra) < 10] + "|")

# Cifrando el mensaje
def cifrado():
    global C, M, x, b, mensaje, alfabeto, cifrado_M
    aux = ''

    M = len(mensaje)
    for letra in mensaje:
        if letra != ' ':
            M = alfabeto.index(letra)
            C = (x*M+b)%len(alfabeto)
            aux = alfabeto[C]
            print('\t\t'+str(letra)+'--> ('+str(x)+'*'+str(M)+'+'+str(b)+') mod '+str(len(alfabeto))+' = '+str(C)+'--> '+aux)
        else:
            aux = ' '
        
        cifrado_M += aux
    
    print("\n\t\tEl mensaje cifrado es: "+cifrado_M)

# Se determina el inverso multiplicativo
def mod_inverse(b, n):
    # Utilizamos el algoritmo extendido de Euclides para encontrar el máximo común divisor de b y n
    r1, r2 = b, n
    s1, s2 = 1, 0
    while r2 > 0:
        q = r1 // r2
        r = r1 - q*r2
        r1, r2 = r2, r
        s = s1 - q*s2
        s1, s2 = s2, s
    
    # Si el máximo común divisor de b y n no es 1, entonces b no tiene inverso multiplicativo módulo n
    if r1 != 1:
        raise ValueError("El número no tiene inverso multiplicativo módulo " + str(n))
    
    # Si el máximo común divisor de b y n es 1, entonces el inverso multiplicativo de b módulo n es s1
    return s1 % n

# Descifrando el mensaje
def descifrado():
    global C, M, x, b, mensaje, alfabeto, cifrado_M
    aux = mensaje = ''
    inverso_multiplicativo = mod_inverse(x, len(alfabeto))
    print('\t\tEl inverso multiplicativo es: '+str(inverso_multiplicativo))

    for letra in cifrado_M:
        if letra != ' ':
            M = alfabeto.index(letra)
            C = (x*M-b)%len(alfabeto)
            aux = alfabeto[C]
            print('\t\t'+str(letra)+'--> ('+str(x)+'*'+str(M)+'-'+str(b)+') mod '+str(len(alfabeto))+' = '+str(C)+'--> '+aux)
        else:
            aux = ' '
        
        mensaje += aux
    
    print("\n\t\tEl mensaje descifrado es: "+mensaje)       

# Función principal
def __main__():
    global mensaje

    print("\t\tAlgoritmo AFIN C=x*M+b")
    
    print("\tEl alfabeto es el siguiente: ")
    alphabet()

    mensaje = input("\tEscribe el mensaje a cifrar: ").upper()

    print("\t\tCIFRANDO...\n\n")
    cifrado()

    print("\n\t\tDESCIFRANDO...\n\n")
    descifrado()

# Ejecutamos la función principal
__main__()
