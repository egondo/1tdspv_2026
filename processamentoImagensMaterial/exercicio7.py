import random


matriz = []
for i in range(30):
    matriz.append([0] * 200)

for i in range(30):
    for j in range(200):
        #matriz[i][j] = random.randint(1, 200)
        matriz[i][j] = random.ra

contagem = [0] * 201

for i in range(30):
    for j in range(200):
        valor = matriz[i][j]
        contagem[valor] = contagem[valor] + 1

for i in range(1, 200):
    print(f"{i} -> {contagem[i]}")