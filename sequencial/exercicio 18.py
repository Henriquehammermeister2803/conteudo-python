tamanho = float(input("digite o tamanho do arquivo em megas:"))
velocidade = float(input("digite a velocidade da internet em mbps:"))

r = tamanho * velocidade
r1 = r / 60
r2 = r1 / 60
print("o tempo de espera é:",r1,"minutos")