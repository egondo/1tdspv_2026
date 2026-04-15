cpf = int(input("Informe o CPF: "))

#separar os digitos de controle
dc = cpf % 100
cpf = cpf // 100

#separar os ultimos 3 digitos
parte3 = cpf % 1000
cpf = cpf // 1000

parte2 = cpf % 1000
cpf = cpf // 1000

parte1 = cpf % 1000

print(f"{parte1:03}.{parte2:03}.{parte3:03}-{dc:02}")