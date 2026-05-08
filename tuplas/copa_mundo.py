def monta_jogos(grupo: tuple) -> tuple:
    resp = (
        f"{grupo[0]} X {grupo[1]}",
        f"{grupo[0]} X {grupo[2]}",
        f"{grupo[0]} X {grupo[3]}",
        f"{grupo[1]} X {grupo[2]}",
        f"{grupo[1]} X {grupo[3]}",
        f"{grupo[2]} X {grupo[3]}",
    )
    return resp


grupo_a = ("México", "República Tcheca", "Coréia do Sul", "África do Sul")

jogos = monta_jogos(grupo_a)
for partida in jogos:
    print(partida)

grupo_brasil = ("Brasil", "Marrocos", "Haiti", "Escócia")
jogos = monta_jogos(grupo_brasil)
for partida in jogos:
    print(partida)
    
