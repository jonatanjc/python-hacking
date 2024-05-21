import random

def adivinar_numero():
    numero_secreto = random.randint(1, 10) 
    intentos = 0

    print("Tienes que adivinar un número entre 1 y 10")

    while True:
        intento = int(input("Introduce tu intento: "))
        intentos += 1

        if intento < numero_secreto:
            print("Demasiado bajo.")
        elif intento > numero_secreto:
            print("Demasiado alto.")
        else:
            print(f"¡Felicidades! ¡Adivinaste el número en {intentos} intentos!")
            break

if __name__ == "__main__":
    adivinar_numero()
