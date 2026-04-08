cons_anterior = float(input("Consumo mês anterior: "))
cons_vigente = float(input("Consumo mês vigente: "))

#decidindo qual o valor por m3
if cons_vigente <= 20:
    valor_m3 = 2.0
elif cons_vigente <= 35:
    valor_m3 = 3.5
elif cons_vigente <= 50:
    valor_m3 = 5.5
else:
    valor_m3 = 7.0

valor_conta = cons_vigente * valor_m3

print(f"valor do consumo: {valor_conta}")

if cons_anterior < cons_vigente:
    multa = valor_conta * 0.10
    print(f"multa: {multa}")
    valor_conta = valor_conta + multa

elif cons_anterior > cons_vigente:
    desconto = valor_conta * 0.15
    print(f"desconto: {desconto}")
    valor_conta = valor_conta - desconto

print(f"total da conta: {valor_conta}")