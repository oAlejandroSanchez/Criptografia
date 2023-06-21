def rc4(key, plaintext):
    S = list(range(256))
    j = 0
    out = []

    # KSA (Key Scheduling Algorithm)
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]

    # PRGA (Pseudo-Random Generation Algorithm)
    i = j = 0
    for char in plaintext:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        k = S[(S[i] + S[j]) % 256]
        out.append(ord(char) ^ k)

    return bytes(out)

def encrypt(key, plaintext):
    ciphertext = rc4(key, plaintext.encode())
    return ciphertext.hex()

def decrypt(key, ciphertext):
    ciphertext = bytes.fromhex(ciphertext)
    plaintext = rc4(key, ciphertext)
    return plaintext.decode()

# Definir la clave y el mensaje
clave = bytes.fromhex("EF CD AB 89 67 54 32 01")
mensaje = "Redes y Seguridad, Criptografía Aplicada a sistemas empotrados de la Facultad de Ingeniería"

# Cifrar el mensaje
mensaje_cifrado = encrypt(clave, mensaje)
print("Mensaje cifrado:", mensaje_cifrado)

# Descifrar el mensaje
mensaje_descifrado = decrypt(clave, mensaje_cifrado)
print("Mensaje descifrado:", mensaje_descifrado)
