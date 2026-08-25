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