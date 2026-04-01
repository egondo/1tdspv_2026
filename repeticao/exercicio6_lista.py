qtd_pes_mal = 0
qtd_pes_med = 0
qtd_pes_bem = 0



nota = int(input("Informe a 1 nota: "))
maior = nota
menor = nota
contador = 1
if nota <= 20:
    qtd_pes_mal = qtd_pes_mal + 1
elif nota <= 50:
    qtd_pes_med = qtd_pes_med + 1
else:
    qtd_pes_bem = qtd_pes_bem + 1

while contador < 20:
    nota = int(input(f"Informe a {contador + 1} nota: "))
    if nota > maior:
        maior = nota
    if nota < menor:
        menor = nota
    if nota <= 20:
        qtd_pes_mal = qtd_pes_mal + 1
    elif nota <= 50:
        qtd_pes_med = qtd_pes_med + 1
    else:
        qtd_pes_bem = qtd_pes_bem + 1

    contador = contador + 1


print(f"A maior nota foi {maior} e a menor foi {menor}")
print(f"% bem {qtd_pes_bem * 100/20}% {qtd_pes_bem}")
print(f"% med {qtd_pes_med * 100/20}% {qtd_pes_med}")
print(f"% mal {qtd_pes_mal * 100/20}% {qtd_pes_mal}")