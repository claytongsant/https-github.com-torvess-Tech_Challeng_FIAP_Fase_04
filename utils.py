import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import locale

# Configurações de locale para datas em português
locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

# Função para carregar dados
def load_data(url):
    df = pd.read_csv(url)
    df['data'] = pd.to_datetime(df['data'], format='%Y-%m-%d')
    return df

# Função para tratamento de dados
def prepare_data(df):
    dias_da_semana = {
        0: 'segunda-feira', 1: 'terça-feira', 2: 'quarta-feira',
        3: 'quinta-feira', 4: 'sexta-feira', 5: 'sábado', 6: 'domingo'
    }
    
    df = df.assign(
        semana_ano=df.data.dt.isocalendar().week,
        dia_semana=df.data.dt.isocalendar().day,
        nome_dia=df.data.dt.isocalendar().day.apply(lambda x: dias_da_semana.get(x)),
        ano=df.data.dt.isocalendar().year,
        mes=df.data.dt.month,
        nome_mes=df.data.dt.strftime('%B')
    )
    return df[['ano', 'mes', 'nome_mes', 'semana_ano', 'dia_semana', 'nome_dia', 'data', 'preco']]

# Função para plotar gráfico de linha
def plot_line_chart(df):
    fig, ax = plt.subplots(figsize=(20, 6))
    sns.set_style("darkgrid")
    ax = sns.lineplot(data=df.groupby('data').agg({'preco': 'mean'}))
    ax.set_title('Evolução do Preço de Petróleo', fontsize=18, weight='bold')
    ax.set_ylabel('Valor Médio')
    ax.set_xlabel('')
    return fig

# Função para plotar boxplot
def plot_boxplot(df):
    fig, ax = plt.subplots(figsize=(20, 6))
    sns.set_style("darkgrid")
    ax = sns.boxplot(data=df, x='ano', y='preco')
    ax.set_title('BoxPlot Preços por Ano', fontsize=18, weight='bold')
    ax.set_ylabel('Preço')
    ax.set_xlabel('')
    return fig