dias_uteis = int(input("Dias úteis: "))
horas_trab = float(input("Horas trabalhadas: "))
valor_hora = float(input("Valor Hora: "))

jornada_devida = dias_uteis * 8
if horas_trab <= jornada_devida:
    #nao tem direito a horas extras
    salario = horas_trab * valor_hora
else:
    horas_extras = horas_trab - jornada_devida
    valor_hora_extra = horas_extras * valor_hora * 1.50
    print(f"Hora Extra: {valor_hora_extra:.2f}")
    salario = jornada_devida * valor_hora + valor_hora_extra

print(f"Total recebido pelo trabalhador foi de {salario:.2f}")
