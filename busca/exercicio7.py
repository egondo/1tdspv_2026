def busca(lista: list, valor) -> list:
    resp = []
    for i in range(len(lista)):
        if lista[i] == valor:
            resp.append(i)
    
    return resp

lst = [2, 5, 7, -1, 4, 2, 5, 3, 19, 18, 16, 16, 15, 13, 11]
resposta = busca(lst, 5)
print(resposta)


resposta = busca(lst, 16)
print(resposta)

resposta = busca(lst, -7)
print(resposta)
