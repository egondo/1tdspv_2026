import Imagem as img

mat = img.getMatrizImagemCinza("domino.png")
lin = len(mat)
col = len(mat[0])

for i in range(lin):
    for j in range(col):
        mat[i][j] = 255 - mat[i][j]

img.salvaImagemCinza("domino_invertido.png", mat)