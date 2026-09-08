import Imagem as img

matriz = img.getMatrizImagemCinza("wallpaper.png")
print(matriz)
#recuperar a dimensao da matriz
lin = len(matriz)
col = len(matriz[0])

print(f"{col} X {lin}")

for i in range(lin):
    for j in range(col):
        matriz[i][j] = matriz[i][j] - 20

img.salvaImagemCinza("wall_escuros.png", matriz)