import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# CONFIGURAÇÃO DA PÁGINA
# ==========================================

st.set_page_config(
    page_title='Dashboard Bancário',
    layout='wide'
)

sns.set_theme(style='darkgrid')

# ==========================================
# TÍTULO
# ==========================================

st.title('Dashboard Bancário - Marketing Campaign')

st.write('Análise interativa do dataset bancário.')

# ==========================================
# IMAGEM
# ==========================================

st.image(
    'https://cdn-icons-png.flaticon.com/512/3135/3135715.png',
    width=120
)

# ==========================================
# FUNÇÃO PARA CARREGAR DADOS
# ==========================================

@st.cache_data
def carregar_dados():
    
    df = pd.read_csv(
        'data/input/bank-additional-full.csv',
        sep=';'
    )
    
    return df

# ==========================================
# FILE UPLOADER
# ==========================================

st.subheader('Upload de novo arquivo')

arquivo = st.file_uploader(
    'Escolha um arquivo CSV',
    type='csv'
)

# ==========================================
# DEFINIÇÃO DO DATAFRAME
# ==========================================

if arquivo is not None:

    try:

        df = pd.read_csv(arquivo, sep=';')

        st.success('Arquivo carregado com sucesso!')

    except Exception as erro:

        st.error(f'Erro ao carregar arquivo: {erro}')

        st.stop()

else:

    df = carregar_dados()

# ==========================================
# VALIDAÇÃO DAS COLUNAS
# ==========================================

colunas_necessarias = [
    'age',
    'job',
    'marital',
    'education'
]

if not all(coluna in df.columns for coluna in colunas_necessarias):

    st.error(
        'O arquivo enviado não possui as colunas necessárias.'
    )

    st.stop()

# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.header('Filtros')

# Slider

idade = st.sidebar.slider(
    'Idade máxima',
    int(df['age'].min()),
    int(df['age'].max()),
    40
)

# Multiselect

job = st.sidebar.multiselect(
    'Profissão',
    df['job'].unique(),
    default=df['job'].unique()
)

marital = st.sidebar.multiselect(
    'Estado Civil',
    df['marital'].unique(),
    default=df['marital'].unique()
)

education = st.sidebar.multiselect(
    'Escolaridade',
    df['education'].unique(),
    default=df['education'].unique()
)

# ==========================================
# FILTRO DOS DADOS
# ==========================================

df_filtrado = df[
    (df['age'] <= idade) &
    (df['job'].isin(job)) &
    (df['marital'].isin(marital)) &
    (df['education'].isin(education))
]

# ==========================================
# RADIO BUTTON
# ==========================================

tipo_grafico = st.radio(
    'Escolha o gráfico:',
    ['Histograma', 'Boxplot']
)

# ==========================================
# COLUMNS
# ==========================================

col1, col2 = st.columns(2)

with col1:

    st.subheader('Dados filtrados')

    st.dataframe(df_filtrado.head())

with col2:

    st.subheader('Informações')

    st.metric(
        'Quantidade de registros',
        len(df_filtrado)
    )

# ==========================================
# FORMULÁRIO
# ==========================================

colunas_numericas = [
    'age',
    'duration',
    'campaign',
    'cons.price.idx'
]

with st.form('formulario'):

    coluna = st.selectbox(
        'Escolha uma coluna numérica',
        colunas_numericas
    )

    botao = st.form_submit_button(
        'Gerar gráfico'
    )

# ==========================================
# GRÁFICOS
# ==========================================

if botao:

    fig, ax = plt.subplots(figsize=(10, 5))

    if tipo_grafico == 'Histograma':

        sns.histplot(
            data=df_filtrado,
            x=coluna,
            kde=True,
            ax=ax
        )

    else:

        sns.boxplot(
            data=df_filtrado,
            x=coluna,
            ax=ax
        )

    st.pyplot(fig)

# ==========================================
# DOWNLOAD
# ==========================================

csv = df_filtrado.to_csv(index=False)

st.download_button(
    label='Baixar dados filtrados',
    data=csv,
    file_name='dados_filtrados.csv',
    mime='text/csv'
)
