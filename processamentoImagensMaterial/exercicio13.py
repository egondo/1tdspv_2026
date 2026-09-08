import Imagem

tupla = Imagem.getMatrizImagemColorida("gato.jpg")
red = tupla[0]
green = tupla[1]
blue = tupla[2]

lin = len(red)
col = len(red[0])

inv_red = []
inv_green = []
inv_blue = []

for i in range(lin):
    inv_red.append([0] * col)
    inv_green.append([0] * col)
    inv_blue.append([0] * col)

for i in range(lin):
    for j in range(col):
        inv_red[lin - 1 - i][col - 1 - j] = red[i][j]
        inv_green[lin - 1 - i][col - 1 - j] = green[i][j]
        inv_blue[lin - 1 - i][col - 1 - j] = blue[i][j]

Imagem.salvaImagemColorida("gato_invertido.jpg", inv_red, inv_green, inv_blue)
print("Processamento realizado")

#Desafio, tente gerar a imagem sem a necessidade de criar outras 3 matrizes, ou seja, 
# tente inverter nas próprias matrizes, claro que vc precisará de uma(s) variavel(is)
# auxiliar(es) 