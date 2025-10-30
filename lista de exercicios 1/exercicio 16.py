import math

area = float(input("Digite o tamanho da área a ser pintada (em m²): "))

litros_necessarios = area / 3
litros_por_lata = 18
preco_por_lata = 80.0


latas_necessarias = math.ceil(litros_necessarios / litros_por_lata)

preco_total = latas_necessarias * preco_por_lata


print(f"\nQuantidade de latas de tinta: {latas_necessarias}")
print(f"Preço total: R$ {preco_total:.2f}")
