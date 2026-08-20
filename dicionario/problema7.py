def menu() -> int:
    print("1 - cadastra")
    print("2 - altera")
    print("3 - médias")
    print("4 - sair")
    return int(input("Opção: "))

def cadastra(turma: dict):
    rm = int(input("RM: "))

    notas = {}  #dicionario que armazenara as notas
    rotulos = ["cp1", "cp2", "cp3", "sp1", "sp2", "gs"]
    for rot in rotulos:
        valor = float(input(f"{rot}: "))
        notas[rot] = valor

    turma[rm] = notas


def calcula_media(turma: dict):
    for notas in turma.values():
        calcula_media_aluno(notas)

    for rm in turma:
        notas = turma[rm]
        print(f"RM {rm} MS: {notas['gs']:.5f}")



def calcula_media_aluno(notas: dict):
    media_sp = (notas['sp1'] + notas['sp2']) / 2
    cp1 = notas['cp1']
    cp2 = notas['cp2']
    cp3 = notas['cp3']

    if cp1 <= cp2 and cp1 <= cp3:
        media_cp = (cp2 + cp3) / 2
    elif cp2 <= cp3 and cp2 <= cp1:
        media_cp = (cp3 + cp1) / 2
    else:
        media_cp = (cp1 + cp2) / 2

    #print(f"CP {media_cp * 2} SP {media_sp * 2}")
    #print(f"GS {notas['gs'] * 6}")
    media_sem = (2 * media_cp + 2 * media_sp + 6 * notas['gs']) / 10
    #print(f"{media_sem:5}")
    notas['ms'] = media_sem


if __name__ == "__main__":
    tdspv = {}
    opcao = menu()
    while opcao != 4:
        if opcao == 1:
            cadastra(tdspv)
        elif opcao == 2:
            print("Nao implementado")
        elif opcao == 3:
            calcula_media(tdspv)
        opcao = menu()