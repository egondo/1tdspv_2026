import random

def gera_senha(tam: int) -> str:
    min = 'abcdefghijklmnopqrstuvwxyz'
    mai = min.upper()
    num = '0123456789'

    senha = ''
    for i in range(tam):
        fonte = random.randint(1, 3)
        if fonte == 1:
            pos = random.randint(0, len(min) - 1)
            senha = senha + min[pos]
        elif fonte == 2:
            pos = random.randint(0, len(mai) - 1)
            senha = senha + mai[pos]
        else:
            pos = random.randint(0, len(num) - 1)
            senha = senha + num[pos]

    return senha

with open("D:/senhas.txt", mode="a") as arq:
    for i in range(100):
        senha = gera_senha(8)
        arq.write(senha)
        arq.write("\n")

print("Fim da gravacao")

