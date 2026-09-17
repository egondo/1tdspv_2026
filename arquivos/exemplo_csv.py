import csv

with open("petr4.csv", mode="r") as arq:
    dados = csv.reader(arq, delimiter=";")
    #print(dados)

    for linha in dados:
        print(linha)