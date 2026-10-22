import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Modo Paisagem",
    layout="wide"  # chave para usar largura total da tela
)

data_frame = pd.read_csv("dados.csv", delimiter=";")

data_frame2 = data_frame[["Categoria", "Produto", "Regiao","Metodo_Pagamento","Faturamento_Total"]]

sumario = pd.pivot_table(data=data_frame2, values='Faturamento_Total', index='Categoria', columns="Regiao", aggfunc="sum")

col1, col2 = st.columns(2)
with col1:
    st.write("Faturamento por regiao e categoria")
    st.write(sumario)

with col2:
    lista_produtos = data_frame2[["Produto"]].drop_duplicates()
    produto = st.selectbox("Escolha o produto", lista_produtos)
    df_produtos = data_frame2.query(f"Produto == '{produto}'")

    df_grafico = pd.pivot_table(data=df_produtos, values="Faturamento_Total", index="Regiao", aggfunc="sum")

    st.bar_chart(df_grafico)

#st.write(df_produtos)




