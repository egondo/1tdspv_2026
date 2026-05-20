import baralho as deck

def get_pontos(mao: list) -> int:
    pontos = 0
    for c in mao:
        if c[0] > 10:
            pontos = pontos + 10
        else:
            pontos = pontos + c[0]
    return pontos

bar = deck.cria_baralho()
deck.embaralha(bar)

mao_hum = deck.distribui(bar, 2)
mao_cpu = deck.distribui(bar, 2)

print(deck.imprime(mao_hum))
print(f"Pontos: {get_pontos(mao_hum)}")
resp = input("Quer mais carta (s/n):")
while resp == 's':
    c = deck.compra(bar)
    mao_hum.append(c)
    print(deck.imprime(mao_hum))
    print(f"Pontos: {get_pontos(mao_hum)}")
    resp = input("Quer mais carta (s/n):")

while get_pontos(mao_cpu) < 16:
    c = deck.compra(bar)
    mao_cpu.append(c)

if get_pontos(mao_hum) < get_pontos(mao_cpu):
    print("Computador venceu!")
else:
    print("Vc venceu!")

print(f"Minhas cartas: {deck.imprime(mao_hum)}")
print(f"Cartas CPU: {deck.imprime(mao_cpu)}")
