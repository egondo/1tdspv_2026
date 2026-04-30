
frase = input("Frase: ")
palavra = input("Palavra: ")

contador = 0

pos = frase.find(palavra, 0)
while pos >= 0:
    contador = contador + 1
    pos = frase.find(palavra, pos + 1)

print(f"{palavra} aparece {contador} vezes em {frase}")