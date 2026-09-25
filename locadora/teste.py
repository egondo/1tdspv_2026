import service

locacao = {
    'retirada': '27/09/2026 14:00',
    'entrega': '30/09/2026 20:00',
    'valor': 0,
    'id_cliente': 1,
    'id_veiculo': 5,
    'status': 'RESERVA',
    'km': 0,
    'id': 21
}

#service.reserva_veiculo(locacao)
#service.retirada_veiculo(locacao)
service.devolucao_veiculo(locacao)

