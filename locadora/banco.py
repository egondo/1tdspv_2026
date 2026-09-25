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
    sql = "SELECT id, marca, modelo, placa, ano, cor, km, valor FROM tb_veiculo ORDER BY modelo"
    
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

def recupera_clientes() -> list:
    sql = "SELECT id, nome, telefone FROM tb_cliente ORDER BY nome"
    lista =[]
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql)
            registros = cur.fetchall()
            for info in registros:
                #cada info, representa um carro que sera representado por um dicionario
                cliente = {'id': info[0], 'nome': info[1], 'telefone': info[2]}
                lista.append(cliente)
    
    return lista


def insere_locacao(locacao: dict):
    sql = "INSERT INTO tb_locacao(id_veiculo, id_cliente, status, retirada, entrega, valor, km) VALUES(:id_veiculo, :id_cliente, :status, to_date(:retirada, 'DD/MM/YYYY HH24:MI'), to_date(:entrega, 'DD/MM/YYYY HH24:MI'), :valor, :km)"
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql, locacao)
        con.commit()


def atualiza_locacao(locacao: dict):
    sql = "UPDATE tb_locacao set id_veiculo= :id_veiculo, id_cliente = :id_cliente, status = :status, retirada = to_date(:retirada, 'DD/MM/YYYY HH24:MI'), entrega = to_date(:entrega, 'DD/MM/YYYY HH24:MI'), valor = :valor, km= :km WHERE id= :id"
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql, locacao)
        con.commit()

def recupera_locacoes(id_cliente: int) -> list:
    sql = "SELECT l.id, to_char(l.retirada, 'DD/MM/YYYY HH24:MI'), to_char(l.entrega, 'DD/MM/YYYY HH24:MI'), l.valor, l.status, v.modelo, v.placa, c.nome, c.telefone, l.id_veiculo, l.id_cliente, l.km, l.valor FROM TB_LOCACAO l JOIN TB_VEICULO v ON l.id_veiculo = v.id JOIN TB_CLIENTE c ON l.id_cliente = c.id WHERE l.id_cliente = :id_cliente AND status = 'RESERVA'"

    with get_conexao() as con:
        with con.cursor() as cur:
            param = {'id_cliente': id_cliente}
            cur.execute(sql, param)
            registros = cur.fetchall()

    lista = []
    for reg in registros:
        loc = {
            'id': reg[0], 'data_retirada': reg[1], 'data_devolucao': reg[2], 'valor': reg[3], 'status': reg[4], 'modelo': reg[5], 'placa': reg[6], 'nome': reg[7], 'telefone': reg[8], 'id_carro': reg[9], 'id_cliente': reg[10], 'km': reg[11], 'valor': reg[12]
        }
        lista.append(loc)
    return lista


def recupera_veiculos_locacao(data1: str, data2: str) -> list:
    sql = '''select id, modelo, marca, placa, ano, valor, km, cor from tb_veiculo WHERE NOT ID IN (SELECT ID_VEICULO FROM TB_LOCACAO WHERE (to_date(:data1, 'DD/MM/YYYY HH24:MI') between retirada and entrega) OR (to_date(:data2, 'DD/MM/YYYY HH24:MI') between retirada and entrega))'''
    lista =[]
    param = {'data1': data1, 'data2': data2}
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql, param)
            registros = cur.fetchall()
            for info in registros:
                carro = converte_carro(info)
                lista.append(carro)
    
    return lista
