Sistema Enquete

A enquete é composta por perguntas, com possibilidade de 
    3 tipos de resposta:
* aberta
* escolha única
* múltipla escolha

Proposta:  Criar uma API para:

* cadastra pergunta
* recupera perguntas
* cadastra respostas (se der tempo)

Como representar em Python uma pergunta?

{
    'numero': 1,
    'texto': 'O que será cobrado no Checkpoint 3?',
    'tipo': 'aberta',
    'escolhas': []
}

{
    'numero': 2,
    'texto': 'Qual a disciplina mais útil que vc aprendeu neste ano?',
    'tipo': 'unica',
    'escolhas': ['CTP', 'DDD', 'Front', 'IA', 'Banco', 'Eng Soft']
}
