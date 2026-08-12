import time

def busca(vet: list, x: int) -> int:
    for i in range(len(vet)):
        if vet[i] == x:
            return i
    return -1

def busca_binaria(vet: list, x: int) -> int:
    ini = 0
    fim = len(vet) - 1
    while ini <= fim:
        meio = (ini + fim) // 2
        if vet[meio] < x:
            ini = meio + 1
        elif vet[meio] > x:
            fim = meio - 1
        else:
            return meio
    return -1

lista = []
for i in range(3_000_000):
    lista.append(i)

ini = time.time()

for i in range(1000):
    pos = busca(lista, -1)
    #print(pos)

fim = time.time()
print(f"Terminou o busca simples: {fim - ini}")


ini = time.time()

for i in range(1000):
    pos = busca_binaria(lista, -1)
    #print(pos)

fim = time.time()
print(f"Terminou o busca binária {fim - ini}")