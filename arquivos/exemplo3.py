#Modo mais economico para leitura de arquivos grandes.
#Apenas uma linha do arquivo será processada

arquivo = "D:/1tdspv_2026/arquivos/info2.txt"

with open(arquivo, mode="r") as arq:
    for linha in arq:
        print(linha)
