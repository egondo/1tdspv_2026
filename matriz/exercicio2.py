import random

matriz = []
for i in range(5):
    matriz.append([0] * 7)

for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        matriz[i][j] = random.randint(0, 1001)

for lin in matriz:
    print(lin)