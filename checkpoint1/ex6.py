x = float(input("X: "))
y = float(input("Y: "))

if x == 0 and y == 0:
    print("Origem")
elif x == 0:
    print("Eixo Y")
elif y == 0:
    print("Eixo X")
elif x > 0 and y > 0:
    print("1 Quad")
elif x < 0 and y > 0:
    print("2 Quad")
elif x < 0 and y < 0:
    print("3 Quad")
else:
    print("4 Quad")