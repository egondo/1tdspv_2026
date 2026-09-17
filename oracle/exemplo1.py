import oracledb

conexao = oracledb.connect(user="pf0313", password="professor#23",      dsn="oracle.fiap.com.br/orcl")

print(f'Database conectado {conexao.version}')

conexao.close()
