def menu() -> int:
    print("SISTEMA DE LOCACAO")
    print("1 cadastra veículo")
    print("2 consulta veículo")
    print("3 sair")
    opcao = int(input("Selecione: "))
    return opcao


banco = []
op = menu()

while op != 3:
    if op == 1: 
        #pedindo os dados do veiculo
        print("Cadastrando veículo")
        placa = input("Placa: ")
        modelo = input("Modelo: ")
        cor = input("Cor: ")
        ano = int(input("Ano: "))
        preco = float(input("Preço: "))

        banco.append(placa)
        banco.append(modelo)
        banco.append(cor)
        banco.append(ano)
        banco.append(preco)

    print(banco)
    print("_" * 40)
    op = menu()
