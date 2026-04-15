#072.509.760-44
#433.862.700-00

cpf9 = int(input("Informe os 9 digitos do cpf: "))

soma1 = 0
soma2 = 0
mult = 2

while cpf9 != 0:
    dig = cpf9 % 10
    soma1 = soma1 + dig * mult
    mult = mult + 1
    soma2 = soma2 + dig * mult
    cpf9 = cpf9 // 10

aux = soma1 % 11
dc1 = 0
if aux >= 2:
    dc1 = 11 - aux

soma2 = soma2 + dc1 * 2

dc2 = 0
aux = soma2 % 11
if aux >= 2:
    dc2 = 11 - aux

print(f"Dígitos de controle {dc1}{dc2}")