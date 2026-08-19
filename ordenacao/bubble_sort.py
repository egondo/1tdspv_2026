def subir(lista: list, i: int):
    pos = len(lista) - 1
    while i < pos:
        if lista[pos] < lista[pos - 1]:
            aux = lista[pos]
            lista[pos] = lista[pos - 1]
            lista[pos - 1] = aux
        pos = pos - 1

def bubble_sort(lista: list):
    for i in range(len(lista)):
        subir(lista, i)

l = [2, 6, -4, 0, 8, 19, 3, 5]
bubble_sort(l)
print(l)
