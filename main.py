
import random
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from datetime import datetime


def executar_acao(estado, acao, saldo, num_acoes, preco):
    
    # Ação de comprar
    if acao == 0:  
        if saldo >= preco:
            num_acoes += 1
            saldo -= preco
    
    # Ação de vender
    elif acao == 1:  
        if num_acoes > 0:
            num_acoes -= 1
            saldo += preco

    # Define o lucro
    lucro = saldo + num_acoes * preco - saldo_inicial

    return (saldo, num_acoes, lucro)


df = pd.read_csv('./data/dataset.csv')

fig = go.Figure(data = [go.Candlestick(x = df['Date'],
                open = df['AAPL.Open'],
                high = df['AAPL.High'],
                low = df['AAPL.Low'],
                close = df['AAPL.Close'])])

fig.show()

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
    
    # Define o saldo
    saldo = saldo_inicial
    
    # Define o número de ações
    num_acoes = num_acoes_inicial

    # Loop
    for i, preco in enumerate(precos[:-1]):
        
        estado = i

        # Escolher a ação usando a política epsilon-greedy
        if np.random.random() < epsilon:
            acao = random.choice(range(len(acoes)))
        else:
            acao = np.argmax(q_tabela[estado])

        # Executar a ação e obter a recompensa e o próximo estado
        saldo, num_acoes, lucro = executar_acao(estado, acao, saldo, num_acoes, preco)
        prox_estado = i + 1

        # Atualizar a tabela Q
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