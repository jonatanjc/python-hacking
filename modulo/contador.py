

def contar_palabras(cadena):
    palabras = cadena.split()
    return len(palabras)

texto = input("Ingresa el texto: ")
numero_palabras = contar_palabras(texto)
print("el texto tiene:", numero_palabras)
