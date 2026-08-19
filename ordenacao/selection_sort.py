def menor(lista: list, pos: int) -> int:
    aux = lista[pos]
    pos_aux = pos
    while pos < len(lista):
        if aux > lista[pos]:
            pos_aux = pos
            aux = lista[pos]
        pos = pos + 1
    return pos_aux

def selection_sort(lista: list):
    for j in range(len(lista) - 1):
        x = menor(lista, j)
        aux = lista[x]
        lista[x] = lista[j]
        lista[j] = aux

lista = [3, 0, -1, 7, 9, 12, 4, 6, 2, 1]
selection_sort(lista)
print(lista)