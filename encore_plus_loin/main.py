
import random
import string

def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

longitud_contrasena = 10
contrasena_aleatoria = generar_contrasena(longitud_contrasena)
print(contrasena_aleatoria)
