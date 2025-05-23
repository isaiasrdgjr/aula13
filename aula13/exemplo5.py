import pandas as pd
import numpy as np

df = pd.read_excel('./aula13/vendas_roupas.xlsx')

# print(df.head(10))
# print(df.describe())

categoria = df['Categoria']
qtd_vendida = df['Unidades Vendidas']

# organiza por unidades vendidas
qtd_organizada = df.sort_values(by='Unidades Vendidas', ascending=True)

media = np.mean(qtd_vendida)
mediana = np.median(qtd_vendida)

print(qtd_vendida)
print(f'{media:.2f}, {mediana:.2f}')

print(qtd_organizada)

print(qtd_vendida.values)

satisfacao = df[df['Satisfação'] == 'Baixo']

print(satisfacao)
