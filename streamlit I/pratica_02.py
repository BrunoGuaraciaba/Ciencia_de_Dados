import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time

# ---------------------------------------------------
# CONFIGURAÇÃO
# ---------------------------------------------------

st.set_page_config(
    page_title="App Completo Streamlit",
    page_icon="📊",
    layout="wide"
)

# ---------------------------------------------------
# TÍTULOS E TEXTOS
# ---------------------------------------------------

st.title("🚀 Aplicação Completa com Streamlit")

st.header("Exemplo de Header")

st.subheader("Exemplo de Subheader")

st.text("Exemplo simples de texto")

st.markdown("### Texto em Markdown")

st.write("Usando st.write()")

st.caption("Exemplo de caption")

st.divider()

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

st.sidebar.title("Menu Lateral")

opcao = st.sidebar.selectbox(
    "Escolha uma opção",
    ["Dados", "Gráficos", "Widgets"]
)

# ---------------------------------------------------
# DADOS
# ---------------------------------------------------

df = pd.DataFrame({
    'coluna1': np.random.randn(100),
    'coluna2': np.random.randn(100),
    'categoria': np.random.choice(['A', 'B', 'C'], 100)
})

st.header("Visualização de Dados")

st.dataframe(df)

st.table(df.head())

st.json({
    "nome": "Bruno",
    "curso": "Ciência de Dados"
})

# ---------------------------------------------------
# MÉTRICAS
# ---------------------------------------------------

st.header("Métricas")

col1, col2, col3 = st.columns(3)

col1.metric("Vendas", "R$ 10 mil", "+5%")
col2.metric("Clientes", "350", "+2%")
col3.metric("Lucro", "R$ 5 mil", "+10%")

# ---------------------------------------------------
# INPUTS
# ---------------------------------------------------

st.header("Widgets")

nome = st.text_input("Digite seu nome")

idade = st.slider("Escolha sua idade", 0, 100, 25)

sexo = st.radio(
    "Sexo",
    ["Masculino", "Feminino"]
)

linguagens = st.multiselect(
    "Linguagens favoritas",
    ["Python", "SQL", "R", "Java"]
)

check = st.checkbox("Aceito os termos")

botao = st.button("Clique aqui")

if botao:
    st.success(f"Olá {nome}")

# ---------------------------------------------------
# SELECTBOX
# ---------------------------------------------------

cidade = st.selectbox(
    "Escolha uma cidade",
    ["São Paulo", "Rio de Janeiro", "Belo Horizonte"]
)

st.write("Cidade escolhida:", cidade)

# ---------------------------------------------------
# DATE INPUT
# ---------------------------------------------------

data = st.date_input("Escolha uma data")

st.write(data)

# ---------------------------------------------------
# FILE UPLOADER
# ---------------------------------------------------

arquivo = st.file_uploader("Envie um arquivo CSV")

if arquivo:
    df_upload = pd.read_csv(arquivo)
    st.dataframe(df_upload.head())

# ---------------------------------------------------
# PROGRESS BAR
# ---------------------------------------------------

st.header("Barra de progresso")

barra = st.progress(0)

for i in range(100):
    time.sleep(0.01)
    barra.progress(i + 1)

# ---------------------------------------------------
# SPINNER
# ---------------------------------------------------

with st.spinner("Carregando..."):
    time.sleep(2)

st.success("Concluído!")

# ---------------------------------------------------
# GRÁFICOS
# ---------------------------------------------------

st.header("Gráficos")

# LINE CHART
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)

st.line_chart(chart_data)

# BAR CHART
st.bar_chart(chart_data)

# AREA CHART
st.area_chart(chart_data)

# ---------------------------------------------------
# MATPLOTLIB
# ---------------------------------------------------

fig, ax = plt.subplots()

sns.histplot(df['coluna1'], bins=20, ax=ax)

st.pyplot(fig)

# ---------------------------------------------------
# MAPA
# ---------------------------------------------------

mapa = pd.DataFrame({
    'lat': [-23.55, -22.90],
    'lon': [-46.63, -43.20]
})

st.map(mapa)

# ---------------------------------------------------
# EXPANDER
# ---------------------------------------------------

with st.expander("Clique para expandir"):
    st.write("Conteúdo escondido")

# ---------------------------------------------------
# TABS
# ---------------------------------------------------

tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])

with tab1:
    st.write("Conteúdo da Tab 1")

with tab2:
    st.write("Conteúdo da Tab 2")

# ---------------------------------------------------
# CONTAINERS
# ---------------------------------------------------

container = st.container()

container.write("Conteúdo dentro do container")

# ---------------------------------------------------
# COLUMNS
# ---------------------------------------------------

col1, col2 = st.columns(2)

with col1:
    st.write("Coluna 1")

with col2:
    st.write("Coluna 2")

# ---------------------------------------------------
# DOWNLOAD BUTTON
# ---------------------------------------------------

csv = df.to_csv(index=False)

st.download_button(
    label="Download CSV",
    data=csv,
    file_name='dados.csv',
    mime='text/csv'
)

# ---------------------------------------------------
# CÓDIGO
# ---------------------------------------------------

codigo = '''
print("Olá mundo")
'''

st.code(codigo, language='python')

# ---------------------------------------------------
# LATEX
# ---------------------------------------------------

st.latex(r'''
a^2 + b^2 = c^2
''')

# ---------------------------------------------------
# FINAL
# ---------------------------------------------------

st.success("Aplicação finalizada com sucesso!")

# ---------------------------------------------------
# CACHE
# ---------------------------------------------------

@st.cache_data
def carregar_dados():
    df_cache = pd.DataFrame({
        'A': np.random.randn(1000),
        'B': np.random.randn(1000)
    })
    return df_cache

dados_cache = carregar_dados()

st.header("Exemplo de Cache")

st.write(dados_cache.head())

# ---------------------------------------------------
# SESSION STATE
# ---------------------------------------------------

st.header("Session State")

if 'contador' not in st.session_state:
    st.session_state.contador = 0

if st.button("Incrementar contador"):
    st.session_state.contador += 1

st.write("Valor do contador:", st.session_state.contador)

# ---------------------------------------------------
# DATA EXPLORER
# ---------------------------------------------------

st.header("Data Explorer")

coluna = st.selectbox(
    "Escolha uma coluna",
    df.columns
)

st.bar_chart(df[coluna].value_counts())

# ---------------------------------------------------
# FORM
# ---------------------------------------------------

st.header("Formulário")

with st.form("meu_formulario"):
    
    email = st.text_input("Email")
    
    senha = st.text_input("Senha", type="password")
    
    enviar = st.form_submit_button("Entrar")

if enviar:
    st.success("Login realizado")

# ---------------------------------------------------
# FILTRO
# ---------------------------------------------------

st.header("Filtro de Dados")

valor = st.slider("Escolha valor máximo", 0, 100, 50)

df_filtrado = df[df.index < valor]

st.dataframe(df_filtrado)