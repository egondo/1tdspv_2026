num = int(input("Informe um número: "))

bin = 0
pot_dez = 1

while num != 0:
    resto = num % 2
    bin = bin + resto * pot_dez
    num = num // 2
    pot_dez = pot_dez * 10

print(f"O numero binário é {bin}")