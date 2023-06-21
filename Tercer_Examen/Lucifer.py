# Universidad Nacional Autónoma de México
# Facultad de Ingeniería

# Asignatura: Criptografía
# Nombre: Alejandro Pérez

# Ejercicio 3: Programar el algoritmo de Luciffer, Cifrar y Descifrar. 10 rondas, 
# sustitución 1 y permutación p=4213. El mensaje será su nombre completo y 
# apellidos. Relleno letra X.

# Alfabeto
alfabeto = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'

# Mensaje
mensaje = ''
mensaje_dividido = []

# Permutación
p = ''

# Sustitución
s = 0

# Números de rondas
rondas = 0

# Se divide el mensaje en secciones de 4 caracteres
def dividir_mensaje():
    global mensaje, mensaje_dividido, p
    aux = ''
    mensaje = mensaje.replace(" ", "")

    # Se agregan caracter
    while len(mensaje)%(len(p)*2) != 0:
        mensaje += 'X'

    for letra in mensaje:
        aux += letra
        if len(aux) == (len(p)*2):
            mensaje_dividido.append(aux)
            aux = ''
    if aux != '':
        mensaje_dividido.append(aux)

# Se cifra el mensaje
def cifrado():
    global mensaje_dividido, p, s, alfabeto, rondas
    s = s%len(alfabeto)
    n1 = n2 = ''
    temp = []
    aux = ''
    
    for contador in range(rondas):
        print("\n\t\tRonda: "+str(contador+1))
        for indice in range(len(mensaje_dividido)):
            n1 = mensaje_dividido[indice][:(len(p))]
            n2 = mensaje_dividido[indice][(len(p)):len(p)*2]
            print("\t\tM["+str(contador+1)+"]: "+n1+'\t'+n2)

            for letra in n1:
                temp.append(alfabeto[(((alfabeto.find(letra)+s)%len(alfabeto)), (alfabeto.find(letra)+s))[(alfabeto.find(letra)+s) < (len(alfabeto)-1)]])
                
            for letra in temp:
                aux += letra

            print("\t\tS["+str(contador+1)+"]: "+aux+'\t'+n2)
            
            aux = ''
            for index in range(len(temp)):
                aux += temp[int(p[index])-1]

            mensaje_dividido[indice] = n2+aux
            print("\t\tP["+str(contador+1)+"]: "+n2+'\t'+aux+"\n")

            aux = ''
            temp = []
    
    print("\t\tMensaje cifrado: ", end='')
    for palabra in mensaje_dividido:
        print(palabra, end='')
    print("\n")

# Se descifra el mensaje
def descifrado():
    global mensaje_dividido, p, s, alfabeto, rondas
    s = s%len(alfabeto)
    n1 = n2 = ''
    temp = []
    aux = ''

    for contador in range(rondas):
        print("\n\t\tRonda: "+str(contador+1))
        for indice in range(len(mensaje_dividido)):
            n2 = mensaje_dividido[indice][:(len(p))]
            n1 = mensaje_dividido[indice][(len(p)):len(p)*2]
            print("\t\tM["+str(contador+1)+"]: "+n1+'\t'+n2)

            for letra in n1:
                temp.append(alfabeto[(((alfabeto.find(letra)-s)%len(alfabeto)), (alfabeto.find(letra)-s))[(alfabeto.find(letra)-s) > (len(alfabeto)-1)]])
                
            for letra in temp:
                aux += letra

            print("\t\tS["+str(contador+1)+"]: "+aux+'\t'+n2)
            
            for index in range(len(aux)):
                temp[int(p[index])-1] = aux[index]
            aux = "".join(letra for letra in temp)
            
            mensaje_dividido[indice] = aux+n2
            print("\t\tP["+str(contador+1)+"]: "+aux+'\t'+n2+"\n")

            aux = ''
            temp = []
    
    print("\t\tMensaje descifrado: ", end='')
    for palabra in mensaje_dividido:
        print(palabra, end='')
    print("\n")

# Función principal
def __main__():
    global mensaje, p, s, rondas

    print("\t\tAlgoritmo de Luciffer")
    mensaje = input("\t\tEscribe el mensaje a cifrar: ").upper().strip()
    p = input("\t\tIndica la permutación: ")
    s = int(input("\t\tIndica la sustitución: "))
    rondas = int(input("\t\tIndica el número de rondas: "))

    # Se divide el mensaje
    dividir_mensaje()

    # Se cifra el mensaje
    cifrado()

    # Se descifra el mensaje
    descifrado()

# Se ejecuta la función principal
__main__()
