import oracledb
import json

with open('carros.json', mode="r") as arq:
    carros = json.load(arq)

conexao = oracledb.connect(user='pf0313', password='professor#23', dsn="oracle.fiap.com.br/orcl")

cursor = conexao.cursor()
sql = "INSERT INTO TB_VEICULO(placa, modelo, ano, cor, marca, km, valor) VALUES(:placa, :modelo, :ano, :cor, :marca, :km, :valor)"

for carro in carros:
    cursor.execute(sql, carro)

conexao.commit()
cursor.close()
conexao.close()
print("Carros inseridos na tabela")
