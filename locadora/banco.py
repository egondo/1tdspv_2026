import oracledb

def get_conexao(usr: str, pwd: str):
    con = oracledb.connect(user=usr, password=pwd, dsn="oracle.fiap.com.br/orcl")
    return con

def get_conexao():
    con = oracledb.connect(user='pf0313', password='professor#23', dsn="oracle.fiap.com.br/orcl")
    return con

def converte_carro(registro: tuple) -> dict:
    car = {
        "id": registro[0],
        "marca": registro[1],
        "modelo": registro[2],
        "placa": registro[3],
        "ano": registro[4],
        "cor": registro[5],
        "km": registro[6],
        "valor": registro[7]
    }
    return car

def recupera_veiculos() -> list:
    sql = "SELECT id, marca, modelo, placa, ano, cor, km, valor FROM tb_cliente ORDER BY modelo"
    
    lista =[]

    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql)
            registros = cur.fetchall()
            for info in registros:
                #cada info, representa um carro que sera representado por um dicionario
                carro = converte_carro(info)
                lista.append(carro)
    
    return lista
