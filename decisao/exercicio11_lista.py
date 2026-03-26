valor = float(input("Valor da compra: "))
print("1 - dinheiro ou cheque, 10% de desconto")
print("2 - cartao de crédito, 5% de desconto")
print("3 - 2x preço normal")
print("4 - 4x acréscimo de 7%")
forma_pgto = int(input("escolha uma das opcoes acima: "))

match forma_pgto:
    case 1:
        desc = valor * 0.1
        print(f"O desconto foi de {desc:.2f}, vc pagara {valor - desc:.2f}")
    case 2:
        desc = valor * 0.05
        print(f"O desconto foi de {desc:.2f}, vc pagara {valor - desc:.2f}")
    case 3:
        parcela = valor / 2
        print(f"Você pagará 2 x {parcela:.2f}")
    case 4:
        acrescimo = valor * 0.07
        parcela = (valor + acrescimo) / 4
        print(f"O valor do produto será de {valor + acrescimo:.2f} em 4 x {parcela:.2f}")
    case _:
        print("Forma de pagamento inválida")