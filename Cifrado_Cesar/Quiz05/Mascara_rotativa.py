# Universidad Nacional Autónoma de México
# Facultad de Ingeniería

# Nombre: Sánchez Pérez Omar Alejandro
# No. de cuenta: 315072264

# Importamos los módulos
import random, re
import numpy as np

# Definimos la función pricnipal
def __main__():
    # Variables:
    alfabeto = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
    tamanioMatriz = 0

    # Título
    print("\t\tMáscara rotativa\n")

    # El usuario puede definir el tamaño de la matriz,
    # siempre y cuando sea mayor a 2x2
    while tamanioMatriz < 2:
        tamanioMatriz = int(input("\tDefine el tamaño de la matriz: "))
        if tamanioMatriz < 2:
            print("\tIntentalo de nuevo\n")

    print("\tLa matriz es de "+str(tamanioMatriz)+"x"+str(tamanioMatriz))
    matriz =  [['/' for _ in range(tamanioMatriz)] for _ in range(tamanioMatriz)]
    auxMatriz = ['/' for _ in range(tamanioMatriz*tamanioMatriz)]

    mensaje = re.sub(" ", "", input("\n\tEscribe el mensaje a cifrar: ").upper())
    print("\n\tIndica las casillas de la máscara rotativa.")
    
    count = 0
    index = 0
    while count < len(matriz):
        index = int(input("\tIndica la columna: "))
        if index < 1 or index > tamanioMatriz:
            print("\tIntentelo de nuevo...")
        else:
            matriz[count][index-1] = '*'
            count += 1
    
    matriz = np.array(matriz)
    
    print("\n\tLa máscara rotativa quedó de la siguiente forma: ")    
    print("\n"+str(matriz))

    print("\n\tPor lo tanto, la matriz con la clave quedó de la siguiente forma: ")
    count = position = 0
    positions = []

    while position <= len(mensaje):
        print(str(len(mensaje)))
        print(position)
        count = 0
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if matriz[i, j] != '*':
                    if not(count in positions):
                        auxMatriz[count] = random.choice(alfabeto)
                else:
                    if(count in positions):
                        break                        
                    #auxMatriz.append(mensaje[position])
                    auxMatriz[count] = mensaje[position]
                    position += 1
                    positions.append(count)
                    
                count += 1

        if position >= len(mensaje):
            break

        matriz = np.rot90(matriz)
        print(matriz)
    
    print(auxMatriz)
    # i = j = count = 0
    # data = []

    # for index in range(4):
    #     for i in range(len(matriz)):
    #         for j in range(len(matriz[i])):
    #             if matriz[i,j] != '*':
    #                 aux[i,j] = random.choice(alfabeto)
    #             else:
    #                 if count >= len(mensaje):
    #                     break
                    
    #                 if len(data) != 0:
    #                     print(str(data[j-1]) + str(data[j]))

    #                 aux[i,j] = mensaje[count]
    #                 count += 1

    #                 data.append(i)
    #                 data.append(j)

    #     if count >= len(mensaje):
    #         break

#   for i in range(len(matriz)):
#         for j in range(len(matriz[i])):
#             if matriz[i,j] != '*':
#                 aux[i,j] = random.choice(alfabeto)
#             else:
#                 aux[i,j] = mensaje[count]
#                 count += 1

# Ejecutamos la función principal
__main__()
