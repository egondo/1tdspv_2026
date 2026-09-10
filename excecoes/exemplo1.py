try:
    num = float(input("Salario: "))
except ValueError:
    print("Digitou um valor incorreto")    
else:
    print(f"Seu salario é {num/1621} salários mínimos")
