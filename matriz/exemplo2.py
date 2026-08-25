matriz = []

#são 4 linhas na matriz
for i in range(4):
    matriz.append([0] * 5)
    #5 colunas

#preenchendo o conteúdo da matriz com os números de 1 a 20
num = 1
for i in range(4):
    for j in range(5):
        matriz[i][j] = num
        num = num + 1        

for lin in matriz:
    print(lin)
