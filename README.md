## Trading-IABOT 

implementação de um agente de negociação usando Q-learning em Python. O objetivo é maximizar o lucro comprando e vendendo ações de uma empresa (neste caso, a Apple) com base nos preços de fechamento históricos.

### Dataset
 São dados relacionados aos preços das ações de uma empresa, especificamente a Apple Inc. As informações incluem a data em que as ações foram negociadas, bem como os preços de abertura, fechamento, alta e baixa das ações da Apple nesse dia. Além disso, a quantidade de ações negociadas (volume) e outras métricas financeiras, como médias móveis e direção da variação dos preços também são fornecidas. Esses dados podem ser usados para análise financeira e para entender o desempenho da Apple no mercado de ações.

### Algoritimo Q-learning

Primeiramente, o código lê os preços de fechamento históricos da Apple de um arquivo CSV e plota um gráfico de velas para visualizar os dados. Em seguida, define os hiperparâmetros do Q-learning, como o número de episódios, a taxa de aprendizado, o fator de desconto e a probabilidade de explorar uma ação aleatória.

O código então inicializa a tabela Q, que é uma matriz que armazena os valores de recompensa para cada ação em cada estado. Em seguida, executa o treinamento do agente por um número fixo de episódios.

Em cada episódio, o agente segue uma política epsilon-greedy para escolher uma ação (comprar, vender ou manter) com base na tabela Q e, em seguida, executa a ação e atualiza a tabela Q com base na recompensa recebida.

Finalmente, o agente é testado em um loop separado, seguindo a política aprendida e executando as ações na série de preços de fechamento históricos. O resultado final é o lucro obtido pelo agente após a negociação de todas as ações disponíveis.


### Dependencias:
- random
- plotly
- pandas
- numpy 
- ipython
- nbformat
- kaleido

Tem o arquivo "requirements.txt" para poder recriar o ambiente virtual com o :
```sh
pip install -r requirements.txt
```
### OBS:
Esse código é apenas um exemplo simples de como implementar um agente de negociação usando Q-learning e deve ser adaptado e ajustado para diferentes casos de uso e mercados financeiros, é apenas para estudo.