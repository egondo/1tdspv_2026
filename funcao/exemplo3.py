def perfeito(num: int) -> bool:
    div = 1
    soma = 0
    while div < num:
        if num % div == 0:
            soma = soma + div
        div = div + 1
    
    if soma == num:
        return True
    else:
        return False


numero = 1
while numero <= 50_000:
    if numero % 10_000 == 0:
        print(numero)
    if perfeito(numero) == True:
        print(numero)
    numero = numero + 1