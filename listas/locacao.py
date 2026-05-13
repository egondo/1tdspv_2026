def menu() -> int:
    print("SISTEMA DE LOCACAO")
    print("1 cadastra veículo")
    print("2 consulta veículo")
    print("3 alterar veículo")
    print("4 vender veículo")
    print("5 locar veículo")
    print("9 sair")
    opcao = int(input("Selecione: "))
    return opcao

def cadastra_veiculo(lista: list):
    #pedindo os dados do veiculo
    print("Cadastrando veículo")
    placa = input("Placa: ")
    modelo = input("Modelo: ")
    cor = input("Cor: ")
    ano = int(input("Ano: "))
    preco = float(input("Preço: "))

    lista.append(placa)
    lista.append(modelo)
    lista.append(cor)
    lista.append(ano)
    lista.append(preco)


def lista_veiculos(lista: list) -> list:
    print("Consulta por valor de locação: ")
    valor = float(input("Digite o valor: "))
    pos = 4
    resultados = []
    while pos < len(lista):
        if lista[pos] <= valor:
            info = f"Placa: {lista[pos-4]} Modelo: {lista[pos-3]} Valor: {lista[pos]}"
            resultados.append(info)
        pos = pos + 5
    return resultados

def altera_veiculo(lista: list, identificacao: str):
    pos = 0
    alterado = False
    while pos < len(lista):
        if lista[pos] == identificacao:
            alterado = True
            print("Alterando dados do veículo: ")
            placa = input(f"Placa ({identificacao}):")
            modelo = input(f"Modelo ({lista[pos + 1]}):")
            cor = input(f"Cor ({lista[pos + 2]}):")
            ano = input(f"Ano ({lista[pos + 3]}):")
            valor = input(f"Valor ({lista[pos + 4]}):")
            if placa: #placa <> ''
                lista[pos] = placa
            
            if modelo != '':
                lista[pos + 1] = modelo

            if cor:
                lista[pos + 2] = cor

            if ano:
                lista[pos + 3] = int(ano)
            
            if valor:
                lista[pos + 4] = float(valor)
            break #encerra o comando de repeticao
        pos = pos + 5
    if alterado:
        print(f"Carro {identificacao} alterado com sucesso!")
    else:
        print(f"Não existe carro com a placa: {identificacao}")


def remove_veiculo(lista: list, placa: str) -> list:
    carro = []
    pos = 0
    while pos < len(lista):
        if lista[pos] == placa:
            carro.append(lista.pop(pos)) #placa
            carro.append(lista.pop(pos)) #modelo
            carro.append(lista.pop(pos)) #cor
            carro.append(lista.pop(pos)) #ano
            carro.append(lista.pop(pos)) #valor
            break
        pos = pos + 5

    return carro


def locar_veiculo(lista: list, placa: str) -> list:
    resp = remove_veiculo(lista, placa)
    locador = input("Locador: ")
    dias = int(input("Dias: "))
    resp.append(locador)
    resp.append(dias)
    return resp        

vendas = []
locacao = []
banco = ['HTE 2343', 'Compass', 'Branca', 2020, 250.0, 'TRE 9256', 'Onix', 'Preta', 2022, 150.0, 'BMW 3432', 'X5', 'Azul', 2023, 600.0]
op = menu()

while op != 9:
    if op == 1: 
        cadastra_veiculo(banco)

    elif op == 2:
        resp = lista_veiculos(banco)
        for carro in resp:
            print(carro)

    elif op == 3:
        placa = input("Placa: ")
        altera_veiculo(banco, placa)

    elif op == 4:
        placa = input("Placa: ")
        veiculo = remove_veiculo(banco, placa)
        for info in veiculo:
            vendas.append(info)

    elif op == 5:
        print("Locacao de veiculos")
        placa = input("Placa: ")
        dados_locacao = locar_veiculo(banco, placa)
        for info in dados_locacao:
            locacao.append(info)

        print(locacao)

    print("_" * 40)
    op = menu()
