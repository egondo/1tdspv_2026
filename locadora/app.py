import banco

def retirada_veiculo():
    clientes = banco.recupera_clientes()
    for cli in clientes:
        print(f"{cli['id']}: {cli['nome']} - {cli['telefone']}")
    id_cliente = int(input("Informe o id do cliente: "))

    locacoes = banco.recupera_locacoes(id_cliente)
    print(f"{locacoes[0]['nome']} - {locacoes[0]['telefone']}")
    for locacao in locacoes:
        print(f"{locacao['id']}: {locacao['modelo']} - {locacao['data_retirada']}")
    id_locacao = int(input("Informe o id da locacao: "))

    data_retirada = input("Data da retirada: ")
    hora_retirada = input("Hora retirada: ")


    for locacao in locacoes:
        if locacao['id'] == id_locacao:
            loc_atual = locacao

    loc_atual['data_retirada'] = f"{data_retirada} {hora_retirada}"
    loc_atual['status'] = 'ANDAMENTO'
    loc_atual.pop('modelo')
    loc_atual.pop('nome')
    loc_atual.pop('telefone')
    loc_atual.pop('placa')
    banco.atualiza_locacao(locacao)




def realiza_reserva_locacao():
    clientes = banco.recupera_clientes()
    for cli in clientes:
        print(f"{cli['id']}: {cli['nome']} - {cli['telefone']}")
    id_cliente = int(input("Informe o id do cliente: "))

    carros = banco.recupera_veiculos()
    for car in carros:
        print(f"{car['id']}: {car['marca']} - {car['placa']}")
    id_carro = int(input("Informe o id do veículo: "))

    data_retirada = input("Data da retirada (dd/mm/aaaa): ")
    hora_retirada = input("Hora da retirada (hh:mm): ")

    data_devolucao = input("Data da devolucao (dd/mm/aaaa): ")
    hora_devolucao = input("Hora da devolucao (hh:mm): ")

    locacao = {
        'id_cliente': id_cliente, 'id_carro': id_carro, 'status': 'RESERVA',
        'data_retirada': f"{data_retirada} {hora_retirada}",
        'data_devolucao': f"{data_devolucao} {hora_devolucao}",
        'valor': 0, 'km': 0 
    }
    banco.insere_locacao(locacao)
    print(f"Locacao realizada com sucesso!")

if __name__ == "__main__":

    #carros = banco.recupera_veiculos()
    #for carro in carros:
    #    print(carro)
    print("1 - Reserva\n2 - Retirada\n3 - Devolucao\n")
    opcao = int(input("Selecione: "))

    if opcao == 1:
        realiza_reserva_locacao()
    elif opcao == 2:
        retirada_veiculo()
    elif opcao == 3:
        pass