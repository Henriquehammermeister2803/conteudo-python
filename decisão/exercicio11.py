sl = float(input("digite su salario:"))
rj1 = 0.2 * sl
rj2 = 0.15 * sl
rj3 = 0.1 * sl
rj4 = 0.05 * sl

if sl <= 1450:
    print("o valor do reajute 1 é:",rj1)

elif sl >= 1451 and sl <= 2800:
    print("seu salario é:",rj2)
    print("você ganhou uma promoção de 15%")
elif sl >= 2801 and sl <= 3500:
    print("seu salario é:",rj3)
    print("você ganhou uma promoção de 20%")
elif sl >= 3500:
    print("seu salario é:",rj4)
    print("você ganhou uma promoção de 5%")

