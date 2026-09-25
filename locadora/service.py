import banco
import datetime
import util



def reserva_veiculo(locacao: dict):
    '''Algumas regras possiveis: 
        * nao faco reservas para clientes que nao aparece
        * verifico se o cliente tem multas
        * verifico se o cliente possui uma CNH válida
    '''
    banco.insere_locacao(locacao)

def retirada_veiculo(locacao: dict):
    '''Algumas regras possiveis: 
        * verifico se existe reserva para o veiculo para o cliente
    ''' 
    #loc = banco.recupera_locacoes(locacao['id_cliente'], locacao['id_veiculo'])

    #if loc == None:
    #    raise Exception(f"Nao existe reserva para o cliente {locacao['id_cliente']}")

    agora = datetime.datetime.now()
    aux = locacao['retirada']
    #converter data retirada para datetime
    retirada = util.str_to_datetime(aux)


    if agora < retirada:
        print("Atualizando a data")        
        locacao['retirada'] = util.datetime_to_str(agora)

    locacao['status'] = 'ANDAMENTO'
    banco.atualiza_locacao(locacao)

def devolucao_veiculo(locacao: dict):
    locacao['status'] = "FINALIZADA"
    agora = datetime.datetime.now()

    #converte data de agora para string
    locacao['entrega'] = util.datetime_to_str(agora)
    
    #gera o valor da locacao com base no carro e na quantidade de tempo
    #que o carro ficou com o cliente
    locacao['valor'] = 400

    banco.atualiza_locacao(locacao)

