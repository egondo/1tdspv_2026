import random

def cria_baralho() -> list:
    monte = []
    for valor in range(1, 14):
        monte.append((valor, '♦️'))
        monte.append((valor, '♣️'))
        monte.append((valor, '♠️'))
        monte.append((valor, '♥️'))
    return monte

def compra(monte: list) -> tuple:
    return monte.pop()

def embaralha(monte: list):
    random.shuffle(monte)

def distribui(monte: list, qtd: int) -> list:
    resp = []
    while qtd > 0:
        resp.append(monte.pop())
        qtd = qtd - 1
    return resp

def to_str(carta: tuple) -> str:
    valor = carta[0]
    naipe = carta[1]
    if valor == 1:
        return f"A{naipe}"
    elif valor == 11:
        return f"J{naipe}"
    elif valor == 12:
        return f"Q{naipe}"
    elif valor == 13:
        return f"K{naipe}"
    else:
        return f"{valor}{naipe}"

def imprime(mao: list) -> str:
    resp = ""
    for carta in mao:
        resp = resp + " " + to_str(carta)
    return resp

#criando uma mao de poquer
#bar = cria_baralho()
#embaralha(bar)
#mao = distribui(bar, 5)
#print(imprime(mao))