# Universidad Nacional Autónoma de México
# Facultad de Ingeniería

# Asignatura: Criptografía
# Nombre: Alejandro Pérez

# Ejercicio 1:
# Programar el algoritmo de Data Encryption Standard

# Se importa el paquete con el algoritmo DES
from Crypto.Cipher import DES

# Función principal
def __main__():
    clave = ''
    mensaje = ''

    print("\n\t\tAlgoritmo Data Encryption Standard")
    clave = bytes(input("\t\tIngresa la clave: "), 'utf-8')
    mensaje = bytes(input("\t\tIngresa el mensaje: "), 'utf-8')

    # Se crea el objeto de cifrado DES
    des = DES.new(clave, DES.MODE_ECB)

    # Se cifra el mensaje
    cifrado = des.encrypt(mensaje)
    print("\t\tEl mensaje quedó cifrado de la siguiente forma: " + str(cifrado))

    # Se descifra el mensaje
    descifrado = des.decrypt(cifrado)
    print("\t\tEl mensaje se ha descifrado: " + str(descifrado) + '\n\n')
    

# Se ejecuta la función principal
__main__()
