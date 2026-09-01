import velha

tab = velha.cria_matriz()
jog = 'X'
while velha.tem_espaco(tab) and not velha.ha_ganhador(tab):
    velha.imprime(tab)
    print(f"Jogador {jog}")
    lin = int(input('lin: '))
    col = int(input("col: "))
    if velha.joga(tab, lin, col, jog):
        jog = 'X' if jog == 'O' else 'O'
        
if velha.ha_ganhador(tab):
    print("Parabéns, tivemos um ganhador!")
else:
    print("Deu velha!")

velha.imprime(tab)