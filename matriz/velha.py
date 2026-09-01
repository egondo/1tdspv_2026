def cria_matriz() -> list:
    mat = []
    for i in range(3):
        mat.append([' '] * 3)
    return mat


def tem_espaco(matriz: list) -> bool:
    for i in range(3):
        for j in range(3):
            if matriz[i][j] == ' ':
                return True
    
    return False    

def ha_ganhador(mat: list) -> bool:
    for i in range(3):
        if mat[i][0] == mat[i][1] and mat[i][1] == mat[i][2] and mat[i][0] != ' ':
            return True
        if mat[0][i] == mat[1][i] and mat[1][i] == mat[2][i] and mat[0][i] != ' ':
            return True
        
    if mat[0][0] == mat[1][1] and mat[1][1] == mat[2][2] and mat[0][0] != ' ':
        return True
        
    if mat[0][2] == mat[1][1] and mat[1][1] == mat[2][0] and mat[0][2] != ' ':
        return True
    return False
    
    

def joga(matriz: list, lin: int, col: int, jogador: str) -> bool:
    if matriz[lin][col] == ' ':
        matriz[lin][col] = jogador
        return True
    else:
        return False

def imprime(matriz: list):
    for lin in matriz:
        print(lin)