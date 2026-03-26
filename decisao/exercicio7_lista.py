import math

numero = float(input("Num: "))

if numero >= 0:
    raiz = math.sqrt(numero)
    print(f"A raiz quadrada de {numero} é igual a {raiz}!")
else:
    print("Impossível extrair raiz de número negativo!")
