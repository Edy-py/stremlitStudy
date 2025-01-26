#importar bibliotecas
import streamlit as st
import pandas as pd
import yfinance as yf

#criar funções


#carregar os dados das ações
@st.cache_data #decorator para salvar os dados em cache
def carregar_dados(empresa):
    texto_tikers = " ".join(empresa)
    dados_acao = yf.Tickers(texto_tikers)
    cotacoes_acao = dados_acao.history(period='1d', start='2010-01-01', end='2025-01-01')
    print(cotacoes_acao)
    cotacoes_acao = cotacoes_acao["Close"]
    return cotacoes_acao

#carregar os tikers
@st.cache_data
def carregar_tikers():
    base_tikers = pd.read_csv("IBOV.csv", sep=";")
    tikers = list(base_tikers["Código"])
    tikers = [item + ".SA" for item in tikers]
    return tikers

acoes = carregar_tikers()
dados = carregar_dados(acoes)

#criar a interface streamlit
st.write(""" # App Preço de ações
         Grafico de linhas dos preços das ações""")

# Criação da sidebar para os filtros
st.sidebar.header("Filtros")

#filtro de ações
lista_acoes = st.sidebar.multiselect("Escolha as Ações", dados.columns)
if lista_acoes:
    dados = dados[lista_acoes]
    if len(lista_acoes) == 1:
        acao_unica = lista_acoes[0]
        dados = dados.rename(columns={acao_unica:"Close"})

#filtro de datas
data_inicial =  dados.index.max().to_pydatetime()
data_final =  dados.index.min().to_pydatetime()
intervalo_datas = st.sidebar.slider("selecione o Periodo",min_value= data_inicial, max_value=data_final, value=(data_inicial, data_final))
dados = dados.loc[intervalo_datas[0]:intervalo_datas[1]]

#visualização do gráfico
st.line_chart(dados)

texto_perfomance_ativos = "" # iniciar string vazia

if len(lista_acoes) == 0:
    lista_acoes = list(dados.columns)
elif len(lista_acoes) == 1:
    dados = dados.rename(columns={"Close": acao_unica})# mudar o nome da coluna

carteira = [1000 for acao in lista_acoes] # criar a carteira utilizando um metodo de list comprehension
total_inicial_carteira = sum(carteira) # sum soma os valores da carteira

for i, acao in enumerate(lista_acoes): # i representa o indice e acao representa o nome da acao
    peformace_ativo = dados[acao].iloc[-1] / dados[acao].iloc[0] - 1 # .iloc[-1] pega o ultimo valor da coluna e .iloc[0] pega o primeiro da coluna
    peformace_ativo = float(peformace_ativo) # converter para float

    carteira[i] = carteira[i] * (1 + peformace_ativo) 

    if peformace_ativo > 0:
        texto_perfomance_ativos += (f"  \n{acao}: :green[{peformace_ativo:.1%}]")
    elif peformace_ativo < 0:
        texto_perfomance_ativos += (f"  \n{acao}: :red[{peformace_ativo:.1%}]")
    else:
        texto_perfomance_ativos += (f"  \n{acao}: {peformace_ativo:.1%}")

# calcular a perfomance da carteira
total_final_carteira = sum(carteira)
peformace_carteira = total_final_carteira / total_inicial_carteira - 1

if peformace_carteira > 0:
    texto_perfomance_carteira = (f"  \nPerfomance da Carteira: :green[{peformace_carteira:.1%}]")
elif peformace_carteira < 0:
    texto_perfomance_carteira = (f"  \nPerfomance da Carteira: :red[{peformace_carteira:.1%}]")
else:
    texto_perfomance_carteira = (f"  \nPerfomance da Carteira: {peformace_carteira:.1%}")


st.write(f"""
### Performace dos Ativos
Essa foi de cada ativo no periodo selecionados:

         
{texto_perfomance_ativos}


{texto_perfomance_carteira}
""")
