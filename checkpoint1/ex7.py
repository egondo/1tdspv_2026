total = float(input("Total das compras: "))

print("Tipo de cliente")
print("1 - Comum")
print("2 - Vip")
print("3 - Premium")
tipo = int(input("Qual é o tipo: "))

desconto = 0
if tipo == 2 and total > 100:
    desconto = total * 0.05
elif tipo == 3:
    if total > 500:
        desconto = total * 0.15
    else:
        desconto = total * 0.10

total = total - desconto

frete = 0
if total < 200:
    frete = 25

print(f"Total da compra: {total}")
print(f"Desconto: {desconto}")
print(f"Frete: {frete}")