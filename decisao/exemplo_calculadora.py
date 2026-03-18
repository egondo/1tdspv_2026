num_a = float(input("Numero a:"))
op = input("Operador (+-*/): ")
num_b = float(input("Numero b:"))

if op == '+':
    print(num_a + num_b)
elif op == '-':
    print(num_a - num_b)
elif op == '*':
    print(num_a * num_b)
elif op == "/":
    if num_b != 0:
        print(num_a / num_b)
    else:
        print("Nao existe / por 0")
