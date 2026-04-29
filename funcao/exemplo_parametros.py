def soma(a: int, b: int) -> int:
    res = a + b
    a = a + 1
    b = b + 1
    return res


x = 5
y = 7
resp = soma(x, y)

print(f"Resposta: {resp}, x={x}, y={y}")