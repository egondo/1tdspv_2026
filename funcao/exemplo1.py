def aumento(valor, percentual):
    novo_valor = (1 + percentual/100) * valor
    #print(novo_valor)
    return novo_valor


new_value = aumento(3500, 15)
print(new_value)
