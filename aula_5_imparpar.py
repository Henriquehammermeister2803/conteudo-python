from difflib import restore

numero = int(input("digite um numero inteiro aleatorio: "))

resto = numero % 2


if resto == 1:
    print("o valor",numero,"é impar")
else: