def particao(lista: list) -> int:
    pivot = lista[0]

    aux = [0] * len(lista)
    ini = 0
    fim = len(aux) - 1
    for i in range(1, len(aux)):
        if lista[i] < pivot:
            aux[ini] = lista[i]
            ini = ini + 1
        else:
            aux[fim] = lista[i]
            fim = fim - 1
    aux[ini] = pivot

    for j in range(len(lista)):
        lista[j] = aux[j]

    return ini

lst = [9, 7, 16, 18, 4, 20, 17, -1, 7, 14]
p = particao(lst)
print(lst)
print("pivo ", p)