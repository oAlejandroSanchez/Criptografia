# Universidad Nacional Autónoma de México
# Facultad de Ingeniería

# Nombre: Sánchez Pérez Omar Alejandro
# No. Cuenta: 315072264

# Asignatura: Criptografía
# Semestre: 2023 - 2

# Ejercicio 2: Programar el algoritmo de Hill, cifrar y descifrar.
# Mostrar el determinante de K y la inversa de la matriz clave.
# Algebra de enteros positivos.

# Importamos los elementos
import re, numpy as np

# Se define la función para determinar el inverso multiplicativo
def inverso_multiplicativo(b, n):
    
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
        raise ValueError("El número no tiene inverso multiplicativo módulo n")
    
    # Si el máximo común divisor de b y n es 1, entonces el inverso multiplicativo de b módulo n es s1
    return s1 % n


# Definimos la función principal
def __main__():
    alfabeto = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'

    # Título
    print("\tCifrado de Hill\n")

    # Se solicita el mensaje
    mensaje = re.sub(" ","",input("\tEscribe el mensaje a cifrar: ").upper())

    while len(mensaje)%3 != 0:
        mensaje += 'X'
    
    # Cifrado del mensaje
    print("\tEn este caso se utilizarán matrices de 3x3, por lo tanto,\n\tel mensaje se dividirá cada 3 carácteres.")
    M = np.array([[0 for _ in range(3)] for _ in range(int(len(mensaje)/3))])

    # Se separa el mensaje en trigramas
    print("\tPor lo tanto el mensaje quedó de la siguiente forma: \n")
    position = 0
    for i in range(len(M)):
        for j in range(len(M[i])):
            M[i, j] = alfabeto.find(mensaje[position])
            position += 1
    
    for i in range(len(M)):
        print("\t" + str(M[i]))

    clave = re.sub(" ", "", input("\n\tIngresa una clave de 9 carácteres: ").upper())

    det = 0
    K = np.array([[0 for _ in range(3)] for _ in range(3)])
    position = 0
    while det == 0:
        if len(clave) > 9:
            clave = clave[:9]
            print(clave)
        elif len(clave) < 9:
            while len(clave) != 9:
                clave += 'A'
        
        for i in range(len(K)):
            for j in range(len(K[i])):
                K[i, j] = alfabeto.find(clave[position])
                position += 1
        
        det = np.linalg.det(K)
        
        if det == 0:
            print("\tIntentalo de nuevo, ya que la determinante es igual a cero.")
            print("\tPor lo tanto, no tiene inversa.")

    # Se imprime en pantala el valor de la determinante y la matriz resultante
    print("\tDeterminate de K = " + str(int(round(det))))
    coprimo = int(round(det))%27
    print("\tPor lo tanto, K mod 27 = " + str(coprimo))

    if int(round(det))%27 != 0:
        print("\tLa matriz tiene inversa con módulo 27...")
        print("\tPor lo tanto, el coprimo de K = " + str(int(round(det))) + " es " + str(coprimo))
    else:
        print("\tLa matriz no es inversa en módulo 27")
        return

    print("\tLa matriz K, quedó de la siguiente forma: \n")
    for i in range(len(K)):
        print("\t" + str(K[i]))
    print()

    aux = np.array([[0 for _ in range(3)] for _ in range(int(len(mensaje)/3))])
    print("\tCifrando el mensaje: \n")
    for i in range(len(M)):
        aux[i] = np.dot(K,M[i])
        for j in range(len(M[i])):
            aux[i,j] = aux[i,j]%27
            if j != 1:
                print("\t" + str(K[j]) + "   " + str(M[i,j]) + "           " + str(aux[i,j]))
            else:
                print("\t" + str(K[j]) + " X " + str(M[i,j]) + " mod(27) = " + str(aux[i,j]))
        
        print()

    print("\tEl mensaje quedó cifrado: ", end = '')
    for i in range(len(aux)):
        for j in range(len(aux[i])):
            print(alfabeto[aux[i,j]], end='')

    print()

    # Se descifra el mensaje
    print("\n\tDescifrando el mensaje: ")
    print("\tLa matriz inversa de K es: \n")
    
    # Calcular la matriz de cofactores
    Adj = np.zeros((3, 3))
    for i in range(3):
        for j in range(3):
            signo = (-1) ** (i+j)
            submatriz = K[np.array(list(range(i))+list(range(i+1, 3))), :]
            submatriz = submatriz[:, np.array(list(range(j))+list(range(j+1, 3)))]
            Adj[i,j] = int(round(signo * np.linalg.det(submatriz)))

    Adj = Adj.T
    print("\t\tPrimero se determina la matriz adjunta, la cual es: ")
    for i in range(len(Adj)):
        print("\t\t" + str(Adj[i]))

    # Se determina el inverso multiplicativo del coprimo
    inverso = inverso_multiplicativo(coprimo,27)
    print("\n\tEl inverso multiplicativo del coprimo es: " + str(inverso))

    # Se multiplica la matriz adjunta por el inverso multiplicativo
    print("\n\tFinalmente, la matriz inversa queda de la siguiente forma: \n")
    K = np.zeros((3, 3))
    for i in range(len(Adj)):
        print("\t",end="")
        for j in range(len(Adj[i])):
            K[i,j] = ((Adj[i,j] * inverso))
            print("\t" + str(K[i,j]), end="")
        print()

    print()

    # Se realiza el descifrado con los componentes ya calculados
    aux2 = np.array([[0 for _ in range(3)] for _ in range(int(len(mensaje)/3))])
    for i in range(len(aux)):
        aux2[i] = np.dot(K,aux[i])
        for j in range(len(aux[i])):
            aux2[i,j] = aux2[i,j]%27
            if j != 1:
                print("\t" + str(K[j]) + "   " + str(aux[i,j]) + "           " + str(aux2[i,j]))
            else:
                print("\t" + str(K[j]) + " X " + str(aux[i,j]) + " mod(27) = " + str(aux2[i,j]))
        print()

    print("\tEl mensaje quedó descifrado: ", end = '')
    for i in range(len(aux2)):
        for j in range(len(aux2[i])):
            print(alfabeto[aux2[i,j]], end='')
    print()

    print("\n\n")

# Se ejecuta la función principal
__main__()
