minimo = 0
maximo = 100
intentos = 0

print("Piensa en un número entre 0 y 100")

while True:
    adivinanza = (minimo + maximo) // 2
    print(f"Intento {intentos + 1}: {adivinanza}", end=" ")
    respuesta = input("(ingresa <, >, o =): ")
    intentos += 1

    if respuesta == "<":
        maximo = adivinanza - 1
    elif respuesta == ">":
        minimo = adivinanza + 1
    elif respuesta == "=":
        print(f"Adiviné en {intentos} intentos")
        break
