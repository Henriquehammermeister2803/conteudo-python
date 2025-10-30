nome = input("digite seu nome: ")

while len(nome) < 3:
    print("o nome precisa ter pelo menos três letras: ")
    nome = input("digite seu nome: ")

idade = int(input("digite sua idade: "))

while idade < 0 or idade > 150:
    print("você não tem essa idade 😒😒, digite uma idade valida ")
    idade = float(input("digite sua idade: "))

salario = float(input("digite o seu salário: "))

while salario <0:
    print("irmão,você não ganha menos que 0 reais")
    salario = float(input("digite seu salario: "))

ECivil =input("digite como está seu estado civil, S = solteiro C = casado V = viuvo D = divorciado ")

while ECivil !="C" and ECivil != "S" and ECivil != "C" and ECivil != "V" and ECivil != "D":
    print("estado civil invalido!")
    input("digite seu estado civil: ")


