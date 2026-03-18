gols_time_a = int(input("Gols Time A: "))
gols_time_b = int(input("Gols Time B: "))

if gols_time_a > gols_time_b:
    print("Time A venceu a partida")
    print(f"{gols_time_a} X {gols_time_b}")
else:
    if gols_time_a < gols_time_b:
        print("Time B venceu a partida")
        print(f"{gols_time_b} X {gols_time_a}")
    else:
        print("Os times empataram")
        print(f"{gols_time_b} X {gols_time_a}")