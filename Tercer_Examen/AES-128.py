from Crypto.Cipher import AES
import binascii


def aes_encrypt(plaintext, key):
    cipher = AES.new(key.encode(), AES.MODE_ECB)
    ciphertext = cipher.encrypt(plaintext.encode())
    return binascii.hexlify(ciphertext).decode()


def aes_decrypt(ciphertext, key):
    cipher = AES.new(key.encode(), AES.MODE_ECB)
    decryptedtext = cipher.decrypt(binascii.unhexlify(ciphertext))
    return decryptedtext.decode()


# Definir el texto en claro y la clave
texto_claro = "ADVANCEDENCRYPTI" 
clave_secreta = "SANCHEZPEREZXXXX"

# Cifrado AES-128
texto_cifrado = aes_encrypt(texto_claro, clave_secreta)

# Descifrado AES-128
texto_descifrado = aes_decrypt(texto_cifrado, clave_secreta)

# Mostrar resultados
print("Texto en claro:", texto_claro)
print("Clave secreta:", clave_secreta)
print("Texto cifrado (en hexadecimal):", texto_cifrado)
print("Texto descifrado:", texto_descifrado)
