n = int(input("Informe n positivo: "))

while n <= 0:
    print("Valor invalido")
    n = int(input("Informe n: "))

soma = 0
num = 1
while num <= n:
    soma = soma + num
    num = num + 1

print(f"A soma vale {soma}")