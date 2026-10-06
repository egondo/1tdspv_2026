import oracledb

def get_conexao():
    return oracledb.connect(user="pf0313", password="professor#23", dsn="oracle.fiap.com.br/orcl")
    

def recupera_time_nome(nome: str) -> dict:
    #escrever a consulta, colocar o parametro, executar a consulta
    #se houver algum time com esse nome, retorno o time na forma de
    #dicionario. 
    #Caso o time não exista, retorno None
    pass

def insere_time(time: dict): 
    #escrevo o comando insert com a opção do oracle devolver o ID
    # que foi gerado para o registro de time
    # pego o id e coloco dentro do dicionario time
    pass

def altera_time(time: dict):
    #escrevo o comando update e atualizo o registro de time com as
    #informações armazenadas no dicionário time
    pass

def insere_partida(partida: dict):
    #escrevo o comando insert e realizo a inserção da partida na tabela partida
    #a tabela partida é composta por: id, nome_mand, id_mand, placar_mand, nome_visi, id_visi, placar_visi
    pass

def recupera_todos_times() -> list:
    #Faço a consulta na tabela times, já calculando: pontos usando a formula: 3 * vitorias + empates, atribuo o nome "pontos" e ordeno em ordem descrescente o resultado da tabela pela coluna pontos
    #retorno a lista de times
    pass