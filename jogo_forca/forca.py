def converte(word: str, letras_chutadas: str) -> str:
    resp = ""
    for c in word:
        if c in letras_chutadas:
            resp = resp + c + " "
        else:
            resp = resp + "_ "
    return resp


palavra = "South Caroline"
err = 0
chutes = ""

segredo = converte(palavra, chutes)
#enquanto nao enforcou e nao acertou:
while err < 6 and "_" in segredo: 
    print(segredo)
    print(f"erros: {err}")
    letra = input("Letra: ")
    chutes = chutes + letra
    if not letra in palavra:
        err = err + 1

    segredo = converte(palavra, chutes)

#Dar a resposta do jogo, seja quando ele acerta ou perde
#Resolver a situação em que a palavra possui letras maiúsculas
#Palavras composta, o programa não mostra o espaço entre as palavras