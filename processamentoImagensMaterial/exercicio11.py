import Imagem

tupla = Imagem.getMatrizImagemColorida("naturezaMorta.jpg")
red = tupla[0]
green = tupla[1]
blue = tupla[2]

lin = len(red)
col = len(red[0])

grey = []
for i in range(lin):
    grey.append([0] * col)

for i in range(lin):
    for j in range(col):
        grey[i][j] = int(0.30 * red[i][j] + 0.59 * green[i][j] + 0.11 * blue[i][j])

Imagem.salvaImagemCinza("naturezaCinza.jpg", grey)
print("Programa executado com sucesso")