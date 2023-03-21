# Universidad Nacional Autónoma de México
# Facultad de Ingeniería

# Nombre: Sánchez Pérez Omar Alejandro
# Asignatura: Criptografía
# Semestre 2023 - 2

# Función que recibe como entrada dos números b y n y devuelve el inverso multiplicativo de b módulo n.
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
        raise ValueError("El número no tiene inverso multiplicativo módulo n")
    
    # Si el máximo común divisor de b y n es 1, entonces el inverso multiplicativo de b módulo n es s1
    return s1 % n

# Definimos la función principal
def __main__():
    # Expresión general
    # a * b mod n = 1
    b = 17   
    n = 2268 
    b_inv = mod_inverse(b, n)

    print("El inverso multiplicativo de {} módulo {} es {}".format(b, n, b_inv))

# Se ejecuta la función principal
__main__()
