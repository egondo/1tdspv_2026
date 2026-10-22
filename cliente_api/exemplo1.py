import requests

if __name__ == "__main__":

    cep = input("CEP: ")
    url = f"https://viacep.com.br/ws/{cep}/json"

    requisicao = requests.get(url)
    dados = requisicao.json()
    print(dados)
