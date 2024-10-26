import streamlit as st
import utils

# Configuração para layout de tela cheia
st.set_page_config(layout="wide")

st.write('## Análise histórico de preços de petróleo 🎲⛽')

# Carregamento dos dados
url = "https://raw.githubusercontent.com/torvess/Tech_Challeng_FIAP_Fase_04/refs/heads/main/Dados/dados_petroleo.csv"
df = utils.load_data(url)

# Preparação dos dados
dados_petroleo = utils.prepare_data(df)

# Gráfico de linha
st.subheader("Evolução do Preço de Petróleo")
fig_line = utils.plot_line_chart(dados_petroleo)
st.pyplot(fig_line)

# Boxplot
st.subheader("BoxPlot Preços por Ano")
fig_boxplot = utils.plot_boxplot(dados_petroleo)
st.pyplot(fig_boxplot)
