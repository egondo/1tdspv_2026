nota = float(input("Nota: "))

while nota < 0 or nota > 10:
    print("Nota inválida")
    nota = float(input("Digite novamente: "))

print(f"A nota inserida foi {nota}")