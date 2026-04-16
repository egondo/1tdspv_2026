frase_a = "Terça é feriado"

frase_b = "Segunda feira nao tem aula"

print(frase_a[0])

print(frase_b[0])

i = 0
vogais = 0
while i < 26:
    if frase_b[i] == 'a' or frase_b[i] == 'e' or frase_b[i] == 'i' or frase_b[i] == 'o' or frase_b[i] == 'u':
        vogais = vogais + 1
    i = i + 1

print(f"A frase b possui {vogais} vogais")