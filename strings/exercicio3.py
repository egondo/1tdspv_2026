frase = input("Frase: ")
letra = input("Letra: ")

letra_upper = letra.upper()
letra_lower = letra.lower()

resultado = ''
for c in frase:
    if c == letra_upper or c == letra_lower:
        resultado = resultado + "*"
    else:
        resultado = resultado + c

print(resultado)