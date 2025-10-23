nm1 = float(input("digite o valor do primeiro produto:"))
nm2 = float(input("digite o valor do segundo produto:"))
nm3 = float(input("digite o valor do terceiro produto:"))

if nm1 < nm2 and nm1 < nm3:
    print("o produto mais barato é: ",nm1)
elif nm2 < nm3 and nm2 < nm1:
    print("o produto mais barato é:",nm2)
else:
    print("o produto mais barato é: ",nm3)