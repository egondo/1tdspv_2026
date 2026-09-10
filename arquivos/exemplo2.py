#Lendo arquivo info.txt

arquivo = "D:/1tdspv_2026/arquivos/info2.txt"

with open(arquivo, mode="r") as arq:
    lista = arq.readlines()

print(lista)
