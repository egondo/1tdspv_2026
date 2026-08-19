def busca(vet: list, x: int) -> int:
    for i in range(len(vet)):
        if vet[i] == x:
            return i
    return -1


def um_de_cada(lista: list) -> list:

    resultado = []
    for elem in lista:
    
        pos = busca(resultado, elem)
        if pos == -1:
            resultado.append(elem)

    return resultado

if __name__ == "__main__":
    lst = [2, 5, 10, 8, 9, 4, 6, 21, 98, 97, 90]
    lista_unica = um_de_cada(lst)
    print(lista_unica) 
