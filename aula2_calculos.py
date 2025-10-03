# arquivo para aprender a realzar calculos com pytom

# sinais mateáticos:
# + soma                 serve para somar valores
# - subtração            serve para diminuir um valor do outro
# * multiplicação        serve para multiplicar valores
# / divisão              serve para dividir um valor pelo outro
# ** potência            serve para fazer a potência de valores
# // divisão inteira     serve para retornar a parte inteira da divisão
# % resto de divisão     serve para retornar o resto da divisão
numero_1 = int(input("digite o primeiro valor:"))
numero_2 = int(input("digite o segundo valor:"))

resultado = numero_1 + numero_2
print("A soma do numero 1 com o numero 2 é:",resultado)

resultado = numero_1 - numero_2
print("A subtração do numero 1 pelo numero 2 é", resultado)

resultado = numero_1 * numero_2
print("A multiplicação do numero 1 pelo numero 2 é",resultado)

resultado = numero_1 / numero_2
print("A divisão do numero 1 pelo numero 2 é",resultado)

resultado = numero_1 ** numero_2
print("A potencia do numero 1 elevado ao numero 2 é",resultado)

resultado = numero_1 // numero_2
print("O numero inteiro do numero 1 pelo numero 2 é",resultado)

resultado = numero_1 % numero_2
print("O resto da divisão do numero 1 pelo numero 2 é",resultado)