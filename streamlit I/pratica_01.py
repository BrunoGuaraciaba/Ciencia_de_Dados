import streamlit as st

st.title("🚀 Meu Primeiro App Streamlit")

st.header("Exemplo de Aplicação")

nome = st.text_input("Digite seu nome")

if st.button("Enviar"):
    st.success(f"Olá {nome}")