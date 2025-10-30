valor_hora = int(input("Quanto você ganha por hora?"))
horas = int(input("Quantas horas você trabalha?"))

print("sabemos que são descontado do seu salario alguns valores")

soma = valor_hora * horas

imposto_de_renda = 0.11
INSS = 0.08
sindicato = 0.05


cauculo_1 = soma * imposto_de_renda
cauculo_2 = soma * INSS
cauculo_3 = soma * sindicato
cauculo_4 = soma - cauculo_1 - cauculo_2 - cauculo_3

print("seu salario bruto é",soma)
print("Você pagou para ao imposto de renda:",cauculo_1)
print("Você pagou para o INSS",cauculo_2)
print("você pagou para o sindicato:",cauculo_3)
print("seu salario liquido é:",cauculo_4)

