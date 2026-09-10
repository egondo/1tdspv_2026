#Lendo arquivo info.txt

arquivo = "D:/1tdspv_2026/arquivos/info.txt"

with open(arquivo, mode="r") as arq:
    content = arq.read()

print(content)