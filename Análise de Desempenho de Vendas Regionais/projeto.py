import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#acessando a planilha para começar a analise
df = pd.read_excel("vendas_regionais.xlsx")
print("-=" * 20)

matriz = df.pivot(index="região", columns="trimestre", values="vendas")
print(matriz)
print("-=" * 20)

#conversão para matriz numpy
array = np.array(matriz)
print("-=" * 20)

#somar vendas por região
soma = np.sum(array, axis=0)
print(soma)
print("-=" * 20)

#clasificar por Alta performance, Necessita atenção e Na média
clasificacao = np.where(soma > np.mean(soma), "Alta performance", np.where(soma < np.mean(soma), "Necessita atenção", "Na média"))
print(clasificacao)
print("-=" * 20)

#estatisticas gerais
ano_mais_lucrativo = np.sort(soma)
print(ano_mais_lucrativo)
print("-=" * 20)

regiao_maior_valor = np.argmax(array, axis=0)
print(regiao_maior_valor)
print("-=" * 20)

regiao_menor_valor = np.argmin(array, axis=0)
print(regiao_menor_valor)
print("-=" * 20)

trimestre_mais_lucrativo = np.argmax(soma)
print(trimestre_mais_lucrativo)
print("-=" * 20)


