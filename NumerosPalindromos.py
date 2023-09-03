def es_palindromo(numero):
    numero_str = str(numero)
    numero_reverso = numero_str[::-1]
    return numero_str == numero_reverso

try:
    numero = int(input("Ingrese un número: "))
    if es_palindromo(numero):
        print(f"{numero} es palíndromo")
    else:
        print(f"{numero} no es palíndromo")
except ValueError:
    print("Entrada inválida. Por favor, ingrese un número entero.")
