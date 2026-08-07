def insere(whats: dict, num_tel: str, msg: str) -> None:
    if num_tel in whats:
        lista_msg = whats[num_tel]
        lista_msg.insert(0, msg)

    else:
        whats[num_tel] = [msg]


def consulta(whats: dict, num_tel: str) -> list:
    if num_tel in whats:
        return whats[num_tel]
    else:
        return None

def menu() -> int:
    print("1 - envia")
    print("2 - consulta")
    print("3 - sair")
    opcao = int(input("Opção: "))
    return opcao

print("Bem vindo ao Whatsapp")    
opcao = 0
whatsapp = {}
while opcao != 3:
    opcao = menu()
    if opcao == 1:
        num = input("Telefone: ")
        msg = input("Msg: ")
        insere(whatsapp, num, msg)
    elif opcao == 2:
        num = input("Telefone: ")
        lista = consulta(whatsapp, num)
        if lista:
            print(lista)
        else:
            print("Contato nao encontrado")
    else:
        print("Saindo do sistema")
