def soma(mata: list, matb: list) -> list:
    lina = len(mata)
    cola = len(mata[0])
    linb = len(matb)
    colb = len(matb[0])
    
    if lina != linb or cola != colb:
        raise Exception('Matrizes com dimensões diferentes')
    resp = []
    for i in range(lina):
        resp.append([0] * cola)
    
    for i in range(lina):
        for j in range(linb):
            resp[i][j] = mata[i][j] + matb[i][j]
    
    return resp


#Exemplo de uso da funcao soma
matx = [
    [3, 5, 7, -2],
    [0, 5, 8, 14],
    [-3, 4, 9, 7]
]

maty = [[-1, 2, 5, 6], [9, 0, 0, 5], [8, -2, 6, -3]]

resultado = soma(matx, maty)
for lin in resultado:
    print(lin)