import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

base_credit = pd.read_csv('../data/credit_data.csv')
# Nessa base de dados, na coluna default o valor 0 indica que a pessoa pagou o empréstimo e 1 indica que a pessoa
# não pagou o empréstimo.

# A coluna id, apesar de ser numérica, fica definida como sendo uma variável categórica nominal.
# A coluna income (renda) é uma variável numérica contínua.
# A coluna age é uma variável numérica contínua. Vale observar que age recebe essa classificação porque no
# arquivo csv em questão, age contém valores de ponto flutante. Se houve somente valores inteiros, age seria
# classificada como variável numérica discreta.
# A coluna loan (empréstimo) é uma variável numérica contínua.
# A coluna default é uma variável numérica discreta (recebe apenas os valores 0 e 1).

# print(base_credit.head()) # Exibe os 5 primeiros registros
# print(base_credit.tail()) # Exibe os 5 últimos registros
# print(base_credit.head(10)) # Exibe os 10 primeiros registros
# print(base_credit.tail(10)) # Exibe os 10 últimos registros

# print(base_credit.describe())
# A linha acima exibe para cada atributo: a contagem total de ocorrências, a média, o desvio padrão, o valor
# mínimo, os 1o., 2o. e 3o. quartis.

# Filtrando os registros com base em certos critérios de seleção
print(base_credit[base_credit['income'] >= 69995.685578])
print(base_credit[base_credit['loan'] <= 1.377630])