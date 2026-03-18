num = int(input("Digite o RM de 5 dígitos"))
soma = 0

un = num % 10
soma = soma + un
num = num // 10

un = num % 10
soma = soma + un
num = num // 10

un = num % 10
soma = soma + un
num = num // 10

un = num % 10
soma = soma + un
num = num // 10

un = num % 10
soma = soma + un
num = num // 10

print("A soma vale", soma)