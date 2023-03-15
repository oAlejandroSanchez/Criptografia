# Universidad Nacional Autónoma de México
# Facultad de Ingeniería

# Nombre: Sánchez Pérez Omar Alejandro
# No. Cuenta: 315072264

# Asignatura: Criptografía
# Semestre: 2023 - 2

# Ejercicio 2: Programar el algoritmo de Hill, cifrar y descifrar.
# Mostrar el determinante de K y la inversa de la matriz clave.
# Algebra de enteros positivos.

# Importando elementos
import re

# Alfabeto
alfabeto = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'

# Mensaje
mensaje = ''
matrizMensaje = []

# Clave
clave = ''
matrizClave = []

# Tamaño de la matriz cuadrada
sizeMatriz = 0

# Imprimimos en pantalla el alfabeto
def printAlphabet(alfabeto):
    for letra in alfabeto:
        print("\t| " + letra + " | " + str(alfabeto.find(letra)) + (" ","  ")[alfabeto.find(letra) < 10] + "|" )
    
    print("")

# Generamos una matriz de nxn (cuadrada) usando la clave
def generateMatrizClave():
    global matrizClave, alfabeto, sizeMatriz, clave
    count = 0
    size = sizeMatriz * sizeMatriz

    if len(clave) < size:
        for index in range(size - len(clave)):
            clave += 'X'
    elif len(clave) > size:
        clave = clave[:size]
    
    for letra in clave:
        


# Obtenemos la clave
def getKey():
    global clave, matrizClave

    # Con re.sub(), se eliminan los espacios de la cadena de carácteres
    clave = re.sub(" ", "", input("\tEscribe la clave: ").upper())

    # Se crea la matriz en función de la clave
    generateMatrizClave()

    # Se imprime la matriz
    printMatriz()

# Obtenemos el mensaje
def getMessage():
    global mensaje

    # Con re.sub(), se eliminan los espacios entre la frase
    mensaje = re.sub(" ", "", input("\tEscribe el mensaje a cifrar. \n\tSin espacios, ni carácteres espciales: ").upper())

# Indicamos el tamaño de la matriz cuadrada
def getSizeMatriz():
    global sizeMatriz

    sizeMatriz = int(input("\tIndica el tamaño de la matriz: "))

# Se imprime la matriz
def printMatriz():
    global matrizClave, sizeMatriz
    count = 0
    print(matrizClave)
    for index in matrizClave:
        print(str(matrizClave[index]))

# Función principal
def main():
    global alfabeto

    # Título
    print("\t\tAlgoritmo de Hill (Ejercicio 2)\n")

    # Se imprime el alfabeto con el valor de cada una de letras
    # de acuerdo a su posición
    printAlphabet(alfabeto)

    # Se obtiene el mensaje
    getMessage()

    # El usuario puede elegir el tamaño de la matriz
    # Es importante aclarar que la matriz es cuadrada, es decir tiene el mismo
    # número de filas que de columnas
    getSizeMatriz()

    # Obtenemos la clave
    getKey()

    # Obtenemos la clave y determinamos si es invertible 
    # a través de determinantes

# Ejecutamos la función principal
main()