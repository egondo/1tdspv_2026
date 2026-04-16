segmento_maximo = 0
contador = 1

n = int(input("Informe o tamanho da sequência: "))
num = int(input("Digite um número: "))

while n > 1:
    ant = num
    num = int(input("Digite um número: "))
    if ant < num:
        contador = contador + 1
    else:
        if contador > segmento_maximo:
            segmento_maximo = contador
        contador = 1
    n = n - 1

if contador > segmento_maximo:
    segmento_maximo = contador
print(f"O segmento máximo da sequencia vale {segmento_maximo}")