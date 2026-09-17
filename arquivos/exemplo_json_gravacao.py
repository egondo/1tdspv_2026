import json

lotofacil = {
    "254": [2, 5, 6, 9, 10, 13, 17, 22],
    "255": [1, 2, 6, 12, 13, 18, 24],
    "256": [1, 3, 5, 10, 14, 15, 21],
    "257": [1, 4, 8, 12, 13, 16, 23],
    "258": [6, 8, 9, 11, 12, 17, 20]
}

with open("lotofacil.txt", mode="w") as arq:
    json.dump(lotofacil, arq, indent=4)

print("arquivo gravado com sucesso")