tamanho = float(input("digite o tamanho do arquivo em megas:"))
velocidade = float(input("digite a velocidade da internet em mbps:"))

r = tamanho * 8
r1 = r / velocidade
print("o tempo de espera é:",r1,"minutos")