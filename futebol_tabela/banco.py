import oracledb

def get_conexao():
    return oracledb.connect(user="pf0313", password="professor#23", dsn="oracle.fiap.com.br/orcl")


def converte(tupla_time: tuple) -> dict:
    time = {
        "id": tupla_time[0],
        "nome": tupla_time[1],
        "vitorias": tupla_time[2],
        "empates": tupla_time[3],
        "jogos": tupla_time[4]
    }
    return time

def recupera_time_nome(nome: str) -> dict:
    #escrever a consulta, colocar o parametro, executar a consulta
    #se houver algum time com esse nome, retorno o time na forma de
    #dicionario. 
    #Caso o time não exista, retorno None
    sql = "SELECT id, nome, vitorias, empates, jogos FROM time WHERE nome = :nome"
    with get_conexao() as con:
        with con.cursor() as cur:
            param = {"nome": nome}
            cur.execute(sql, param)
            dados = cur.fetchone()
            if dados:
                return converte(dados)
    return None

def insere_time(time: dict):  
    #escrevo o comando insert com a opção do oracle devolver o ID
    # que foi gerado para o registro de time
    # pego o id e coloco dentro do dicionario time
    sql = "INSERT INTO time(nome, vitorias, empates, jogos) VALUES(:nome, :vitorias, :empates, :jogos) RETURNING id INTO :id"

    with get_conexao() as con:
        with con.cursor() as cur:
            newid = cur.var(oracledb.NUMBER)
            time['id'] = newid
            cur.execute(sql, time)
            time['id'] = newid.getvalue()[0]
        con.commit()


def altera_time(time: dict):
    #escrevo o comando update e atualizo o registro de time com as
    #informações armazenadas no dicionário time
    sql = "UPDATE time set nome=:nome, vitorias=:vitorias, empates=:empates, jogos=:jogos WHERE id=:id"

    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql, time)
        con.commit()


def recupera_todos_times() -> list:
    #Faço a consulta na tabela times, já calculando: pontos usando a formula: 3 * vitorias + empates, atribuo o nome "pontos" e ordeno em ordem descrescente o resultado da tabela pela coluna pontos
    #retorno a lista de times
    sql = "SELECT NOME, VITORIAS * 3 + EMPATES as PONTOS, VITORIAS, EMPATES, JOGOS - VITORIAS - EMPATES as DERROTAS, JOGOS FROM TIME ORDER BY PONTOS DESC"
    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql)
            lista = cur.fetchall()

    resp = []
    for tupla in lista:
        time = {
            "nome": tupla[0],
            "pontos": tupla[1],
            "vitorias": tupla[2],
            "empates": tupla[3],
            "derrotas": tupla[4],
            "jogos": tupla[5]
        }
        resp.append(time)
    return resp



def insere_partida(partida: dict):
    #escrevo o comando insert e realizo a inserção da partida na tabela partida
    #a tabela partida é composta por: id, nome_mand, id_mand, placar_mand, nome_visi, id_visi, placar_visi
    sql = "INSERT INTO partida(nome_mand, id_mand, placar_mand, nome_visi, id_visi, placar_visi) VALUES(:mandante, :id_mand, :placar_m, :visitante, :id_visi, :placar_v)"

    with get_conexao() as con:
        with con.cursor() as cur:
            cur.execute(sql, partida)
        con.commit()
