import re

def is_numero_regex(valor: str) -> bool:
    match = re.search("^-?[0-9]+\.?[0-9]+$", valor)
    if match == None:
        return False
    else:
        return match.string == valor    


def is_numero(valor: str) -> bool:
    if valor.isnumeric():
        return True
    else:
        if valor[0] == '-' and not '.' in valor:
            return valor[1:].isnumeric()
        elif valor[0] != '-' and '.' in valor:
            return valor.replace('.', '').isnumeric()
        elif valor[0] == '-' and '.' in valor:
            return valor[1:].replace('.', '').isnumeric()
        else:
            return False
            




valor = input("Informe um valor: ")

if valor.isnumeric():
    print(f"{valor} pode ser convertido para numero")
else:
    print(f"{valor} nao pode ser convertido para numero")
