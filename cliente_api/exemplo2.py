import requests

print("Cadastra PARTIDA")
mand = input("Mandante: ")
gol_m = int(input("Gols do mandante: "))

visi = input("Visitante: ")
gol_v = int(input("Gols do visitante: "))

dado = {
    "mandante": mand, "placar_m": gol_m, "placar_v": gol_v, "visitante": visi
}

url = 'https://onetdspv-2026.onrender.com/api/v1/partidas'
requisicao = requests.post(url, json=dado)
if requisicao.status_code >= 200 and requisicao.status_code < 300:
    print("Partida cadastrada com sucesso!")
else:
    print("Deu erro no cadastro!")
#print(requisicao.json())

url = 'https://onetdspv-2026.onrender.com/api/v1/times'
requisicao = requests.get(url)
tabela = requisicao.json()

print("|time|pontos|vitorias|empates|derrotas|jogos|")
print("|:---|---:|---:|---:|---:|---|")

for time in tabela:
    print(f"|{time['nome']}|{time['pontos']}|{time['vitorias']}|{time['empates']}|{time['derrotas']}|{time['jogos']}|")