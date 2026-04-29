def mdc(a: int, b: int) -> int:
    pass

def mmc(a: int, b: int) -> int:
    resp = a
    while resp % b != 0:
        resp = resp + a

    return resp

resultado = mmc(14, 6)
print(resultado)

resultado = mmc(6, 14)
print(resultado)