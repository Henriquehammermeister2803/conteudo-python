

litros = float(input("quantos litros voce quer abastecer? "))

comb = input("qual é o combustivel que voce quer? A = alcool G = gasolina")

match comb:
    case "A":
        if litros > 20:
            pct_desconto = 5
        else:
            pct_desconto = 3

        val_total = litros * 4.17
        val_desconto = val_total * (pct_desconto/100)
        val_liquido = val_total - val_desconto

        print(f"voce vai pagar R${val_liquido}")
        print(f"voce teve {pct_desconto}% de desconto, economizando R${val_desconto}")

    case _:
        