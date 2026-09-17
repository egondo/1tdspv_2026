import oracledb

conexao = oracledb.connect(user="pf0313", password="professor#23",      dsn="oracle.fiap.com.br/orcl")

sql = "SELECT * FROM TB_VEICULO"

cursor = conexao.cursor()
cursor.execute(sql)
dados = cursor.fetchall()
cursor.close()
conexao.close()

for registro in dados:
    print(registro)
