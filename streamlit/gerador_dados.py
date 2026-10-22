import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Configuração para reprodutibilidade
np.random.seed(42)

# 1. Definindo os parâmetros dos dados
n_linhas = 1000
data_inicial = datetime(2025, 1, 1)

Categorias = ['Eletrônicos', 'Vestuário', 'Alimentos', 'Home & Office', 'Beleza']
produtos = {
    'Eletrônicos': ['Smartphone', 'Notebook', 'Fone Bluetooth', 'Smartwatch'],
    'Vestuário': ['Camiseta', 'Calça Jeans', 'Tênis Esportivo', 'Jaqueta'],
    'Alimentos': ['Café Gourmet', 'Chocolate Artesanal', 'Suplemento', 'Snacks'],
    'Home & Office': ['Cadeira Ergonômica', 'Luminária LED', 'Teclado Mecânico', 'Mouse Sem Fio'],
    'Beleza': ['Perfume Importado', 'Creme Hidratante', 'Protetor Solar', 'Kit Maquiagem']
}
regioes = ['Sudeste', 'Nordeste', 'Sul', 'Centro-Oeste', 'Norte']
pagamentos = ['Cartão de Crédito', 'Pix', 'Boleto Bancário', 'Vale Refeição']

# 2. Gerando os dados sintéticos
datas = [data_inicial + timedelta(days=int(np.random.randint(0, 365)), 
                                  hours=int(np.random.randint(0, 24)), 
                                  minutes=int(np.random.randint(0, 60))) 
         for _ in range(n_linhas)]

lista_categorias = np.random.choice(Categorias, size=n_linhas)
lista_produtos = [np.random.choice(produtos[cat]) for cat in lista_categorias]
lista_regioes = np.random.choice(regioes, size=n_linhas)
lista_pagamentos = np.random.choice(pagamentos, size=n_linhas)

quantidades = np.random.randint(1, 6, size=n_linhas)
precos_unitarios = np.round(np.random.uniform(15.0, 350.0, size=n_linhas), 2)
faturamento = np.round(quantidades * precos_unitarios, 2)
custo_logistica = np.round(faturamento * np.random.uniform(0.05, 0.20, size=n_linhas), 2)
avaliacao_cliente = np.random.randint(1, 6, size=n_linhas)

# 3. Criando o DataFrame do Pandas
df_dashboard = pd.DataFrame({
    'ID_Pedido': [f'REQ-{i+10000}' for i in range(n_linhas)],
    'Data_Venda': datas,
    'Categoria': lista_categorias,
    'Produto': lista_produtos,
    'Regiao': lista_regioes,
    'Metodo_Pagamento': lista_pagamentos,
    'Preco_Unitario': precos_unitarios,
    'Quantidade': quantidades,
    'Faturamento_Total': faturamento,
    'Custo_Frete': custo_logistica,
    'Avaliacao_Cliente': avaliacao_cliente
})

# 4. Ordenando por data
df_dashboard = df_dashboard.sort_values(by='Data_Venda').reset_index(drop=True)

# 5. Salvando em CSV (opcional, comum para alimentar dashboards)
df_dashboard.to_csv('massa_dados_dashboard.csv', index=False, sep=';', encoding='utf-8-sig')

# Visualizando o resultado
print(df_dashboard.head())
