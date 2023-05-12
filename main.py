
import random
import plotly.graph_objects as go
import pandas as pd
import numpy as np


def executar_acao(estado, acao, saldo, num_acoes, preco):
    
    if acao == 0:  
        if saldo >= preco:
            num_acoes += 1
            saldo -= preco
    
    elif acao == 1:  
        if num_acoes > 0:
            num_acoes -= 1
            saldo += preco

    lucro = saldo + num_acoes * preco - saldo_inicial

    return (saldo, num_acoes, lucro)


df = pd.read_csv('./data/dataset.csv')

import plotly.graph_objects as go

fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['AAPL.Open'],
                high=df['AAPL.High'],
                low=df['AAPL.Low'],
                close=df['AAPL.Close'])])

fig.write_image("./img/candlestick.png", format="png")


fig.show(renderer="svg", include_plotlyjs=False)

precos = df['AAPL.Close'].values

print('\nDefinindo os Hiperparâmetros do Q-Learning...')
num_episodios = 1000
alfa = 0.1
gama = 0.99
epsilon = 0.1

print('\nConfigurando o Ambiente de Negociação...')
acoes = ['comprar', 'vender', 'manter']
saldo_inicial = 1000
num_acoes_inicial = 0

print('\nInicializando a Tabela Q...')
q_tabela = np.zeros((len(precos), len(acoes)))

print('\nInicializando o Treinamento...')
for _ in range(num_episodios):
    
    saldo = saldo_inicial
    
    num_acoes = num_acoes_inicial

    for i, preco in enumerate(precos[:-1]):
        
        estado = i

        if np.random.random() < epsilon:
            acao = random.choice(range(len(acoes)))
        else:
            acao = np.argmax(q_tabela[estado])

        saldo, num_acoes, lucro = executar_acao(estado, acao, saldo, num_acoes, preco)
        prox_estado = i + 1

        q_tabela[estado][acao] += alfa * (lucro + gama * np.max(q_tabela[prox_estado]) - q_tabela[estado][acao])

print('\nTreinamento Concluído...')

saldo = saldo_inicial
num_acoes = num_acoes_inicial

print('\nExecutando o Agente...')
for i, preco in enumerate(precos[:-1]):
    estado = i
    acao = np.argmax(q_tabela[estado])
    saldo, num_acoes, _ = executar_acao(estado, acao, saldo, num_acoes, preco)
    
print('\nExecução Concluída...')

saldo += num_acoes * precos[-1]
lucro = saldo - saldo_inicial
lucro_final = round(lucro,2)

print(f"\nComeçamos a Negociação com Saldo Inicial de 1000 e Tivemos Lucro de: {lucro_final}")

print("\nObrigado Por Usar o Robô Trading.\n")

