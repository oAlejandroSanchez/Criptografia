# Universidad Nacional Autónoma de México
# Facultad de Ingeniería

# Asignatura: Criptografía
# Nombre: Alejandro Pérez

# Tarea 08: Desarrollar un LFSR de 8 bits

# Número de bits
bits = 0
# Polinomio primitivo
polinomio = ""
# Semilla
semilla = ""


# Se define la función principal
def __main__():
    global bits, polinomio, semilla

    print("\n\t\tLFSR (n bits)\n")
    # Se debe indicar el número de bits
    try:
        bits = int(input("\tIndica el número de bits: "))
    finally:
        print("\tIntentalo de nuevo")

    # Se verifica si el número de bits es mayor a cero
    if bits <= 0 :
        print("\tEl número de bits debe ser mayor a cero...")
        return
    
    # Se debe indicar el polinomio primitivo
    n = bits
    print("\tIndica el tipo de polinomio con 1 y 0")
    print("\n\t", end="")
    for i in range(bits):
        print(("X","X^" + str(n))[n > 1], end="+")
        n -= 1
    print("1", end="")

    polinomio = input("\tPolinomio primitivo: ")

    if len(polinomio) < bits:
        for i in range(bits - len(polinomio)):
            polinomio = polinomio + "0"
    elif len(polinomio) > bits:
        polinomio = polinomio[:bits]

    semilla = input("\n\tEscribe la semilla: ")

    secuencia_maxima = (2 ** bits)-1
    print("\n\tLa longitud máxima es: " + str(secuencia_maxima))

    # Se realiza la secuencia pseudo aleatoria
    secuencia_final = ""
    aux = ""
    secuencia = semilla
    position = [indice for indice, dato in enumerate(polinomio) if dato == "1"]
    primer_elemento = position.pop(0)
    contador = 0
    
    while(1):
        # Se incrementa el contador
        contador += 1

        # Se realiza la operación XOR
        aux = secuencia[int(primer_elemento)]
        for indice in range(len(position)):
            if secuencia[int(position[indice])] == aux:
                aux = "0"
            else: 
                aux = "1"
        
        # Se guarda el valor y se imprime en pantalla el valor
        secuencia_final += secuencia[-1]
        print("\t" + str(contador) + ": " + secuencia + " --> " + secuencia[-1])

        # Se recorre el bit y se agrega el dato aux al inicio de la cadena
        secuencia = aux + secuencia[:-1]

        # Se determina el final del ciclo
        if(secuencia == semilla):
            break
        
    # Se imprime la cadena final
    print("\n\tLa secuencia final es: " + secuencia_final, end="\n\n")

# Se ejecuta la función principal
__main__()
