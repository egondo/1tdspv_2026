import oracledb

create = '''
create table livro(
    id number generated always as identity,
    titulo varchar(100),
    autor varchar(50),
    categoria varchar(50),
    quantidade number(4, 0),
    valor number(6, 2),
    primary key(id))
'''

def get_conexao():
    return oracledb.connect(user="pf0313", password="professor#23", dsn="oracle.fiap.com.br/orcl")

def insere_livro(livro: dict):
    sql = "INSERT INTO livro(titulo, autor, categoria, quantidade, valor) VALUES(:titulo, :autor, :categoria, :quantidade, :valor) returning id into :id"

    with get_conexao() as con:
        with con.cursor() as cur:
            new_id = cur.var(oracledb.NUMBER)
            livro['id'] = new_id
            cur.execute(sql, livro)
            livro['id'] = new_id.getvalue()[0]
        con.commit()

