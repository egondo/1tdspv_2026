import math

a = float(input("A: "))
b = float(input("B: "))
c = float(input("C: "))

if a == 0:
    print("Não é equacao de segundo grau")
else:
    delta = b * b - 4 * a * c
    if delta < 0:
        print("A equacao nao possui raizes reais!")
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)  
        print(f"As raizes da equacao sao {x1} e {x2}")