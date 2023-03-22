import numpy as np

# Definir la matriz
matriz = np.array([[2, 0, 1], [3, 0, 0], [5, 1, 1]])

# Calcular la matriz de cofactores
cofactores = np.zeros((3, 3))
for i in range(3):
    for j in range(3):
        signo = (-1) ** (i+j)
        submatriz = matriz[np.array(list(range(i))+list(range(i+1, 3))), :]
        submatriz = submatriz[:, np.array(list(range(j))+list(range(j+1, 3)))]
        cofactores[i,j] = signo * np.linalg.det(submatriz)

# Transponer la matriz de cofactores para obtener la adjunta
adjunta = cofactores.T

print(adjunta)
