saque = int(input("digite o valor a ser sacado"))

if saque < 10 or saque > 600:
    print("não é possivel sacar o valor informado")
    exit(1)

qtd_cem = 0
qtd_cinquenta = 0
qtd_dez = 0
qtd_cinco = 0
qtd_um = 0