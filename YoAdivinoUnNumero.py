import random

numero = random.randint(0, 100)
intentos = 0

print("Adivina el número entre 0 y 100")

while True:
    try:
        adivinanza = int(input(f"Intento {intentos + 1}: "))
        intentos += 1

        if adivinanza < numero:
            print(f"Es mayor que {adivinanza}")
        elif adivinanza > numero:
            print(f"Es menor que {adivinanza}")
        else:
            print(f"Correcto. Adivinaste en {intentos} intentos")
            break
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número entero.")
