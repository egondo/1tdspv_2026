import banco

#partida = {
#    "mandante": "Vasco da Gama",
#    "visitante": "Cruzeiro",
#    "placar_m": 2,
#    "placar_v": 1
#}

def resolve_time(nome: str, vit: int, emp: int) -> dict:
    time = banco.recupera_time_nome(nome)
    if not time:
        time = {"nome": nome, "vitorias": vit, "empates": emp, "jogos": 1}
        banco.insere_time(time)
    else:
        time['jogos'] = time['jogos'] + 1
        time['vitorias'] = time['vitorias'] + vit
        time['empates'] = time['empates'] + emp
        banco.altera_time(time)
    return time


def cadastra_partida(partida: dict):
    vit_mand = vit_vis = emp_mand = emp_visi = 0

    if partida['placar_m'] > partida['placar_v']:
        vit_mand = 1
    elif partida['placar_m'] < partida['placar_v']:
        vit_visi = 1
    else:
        emp_mand = 1
        emp_visi = 1
    
    time_mand = resolve_time(partida['mandante'], vit_mand, emp_mand)
    time_visi = resolve_time(partida['visitante'], vit_visi, emp_visi)

    partida['id_mand'] = time_mand['id']
    partida['id_visi'] = time_visi['id']
    banco.insere_partida(partida)


def recupera_times():
    return banco.recupera_todos_times()
