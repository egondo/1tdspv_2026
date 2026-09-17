import json

with open("dados.json", mode="r") as arq:
    dados = json.load(arq)

for disciplina in dados:
    print(disciplina['professor'], disciplina['nome'])

