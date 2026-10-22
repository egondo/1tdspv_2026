import streamlit as st

col1, col2 = st.columns(2)
with col1:
    nome = st.text_input("Digite o seu nome: ")
    idade = st.number_input("Idade: ", value=18, min_value=0, max_value=120)

    disciplina = st.radio("Qual a disciplina mais chata?", ["CTP", "DDD", "Front", "Banco", "IA"], captions=["Computational Thinking", "Domain Drive Design", "Frontend", "Database", "IA Chatbot"])
    
    botao = st.button("ok")

with col2:
    if botao:
        st.write(f"Olá {nome}, você tem {idade} anos")
        st.write(f"Vc escolheu {disciplina}")

