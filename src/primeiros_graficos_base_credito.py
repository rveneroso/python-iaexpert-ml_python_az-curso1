import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

base_credit = pd.read_csv('../data/credit_data.csv')
# Para saber quais valores distintos existem no atributo default
# print(np.unique(base_credit['default'])) # Imprime os valores em forma de array [0 1]
# Para retornar o número de ocorrências em cada um dos atributos distintos:
# print(np.unique(base_credit['default'], return_counts=True)) # Imprime (array([0, 1]), array([1717,  283]))
# Gerando um gráfico com os totais para clientes que pagam e que não pagam o empréstimo.
# sns.countplot(x = base_credit['default']);
# Plotando um gráfico que separa as idades por faixas
# plt.hist(x = base_credit['age']);
# Gerando um gráfico que contabiliza os registros baseado na renda agrupando por faixas.
# plt.hist(x = base_credit['income']);
# Gerando um gráfico que contabiliza os registros baseado na renda agrupando por faixas.
# plt.hist(x = base_credit['loan']);
# plt.show()
# Gera um gráfico de dispersão combinando os valores dos atributos age, income e loan 2 a 2. Há um gráfico
# que combina cada atributo com ele mesmo (são os gráficos que geram um reta). O parâmetro
# color = 'default' irá plotar o gráfico um uma cor para os registros em que default = 0 e outra cor para
# os registros em que default = 1.
# Observação: ao executar esse script, o gráfico foi exibido em uma aba no browser aberta pelo próprio
# PyCharm.
grafico = px.scatter_matrix(base_credit, dimensions=['age', 'income', 'loan'], color = 'default')
grafico.show()