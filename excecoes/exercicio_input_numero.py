'''Faca um controle de digitacao de valores numericos usando o
controle de excecoes, ou seja, enquanto o usuario informar
uma entrada que nao possa ser convertida para numero real o
seu programa nao continua a execucao'''

digita_correto = False
while not digita_correto:
    try:
        salario = float(input("Digite o salario: "))
        print(salario)
        digita_correto = True
    except:
        print("Digite corretamente o salario")
    #else:
    #    digita_correto = True
