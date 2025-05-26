import pandas as pd
import numpy as np
import os

df = pd.read_excel('./aula13/vendas_eletronicos.xlsx')

qtd_vendidas = df['Unidades Vendidas']
tot_faturamento = df['Faturamento Total (R$)']

media_vendas = np.mean(qtd_vendidas)
mediana_vendas = np.median(qtd_vendidas)
media_fat = np.mean(tot_faturamento)
mediana_fat = np.median(tot_faturamento)

os.system('clear')
print(f'As médias foram de {media_vendas:.2f} vendas e R${media_fat:.2f} de farutamento')
print(f'As medianas foram de {mediana_vendas:.2f} vendas R${mediana_fat:.2f} de faturamento')

q1 = np.quantile(qtd_vendidas, 0.25)
q2 = np.quantile(qtd_vendidas, 0.50)
q3 = np.quantile(qtd_vendidas, 0.75)

print(f'\nOs produtos que ficaram abaixo de {q1} vendas, podem estar com pouca procura') 
print(f'Os produtos que ficaram entre {q1} e {q2} de vendas, tiveram um desempenho regular de vendas')
print(f'Os produtos que ficaram entre {q1} e {q3} de vendas, tiveram bom desempenho de vendas')
print(f'Os produtos que venderam mais de {q3} unidades, tiveram um desempenho excelente de vendas')

q1_totalfat = np.quantile(tot_faturamento, 0.25)
q2_totalfat = np.quantile(tot_faturamento, 0.50)
q3_totalfat = np.quantile(tot_faturamento, 0.75)

mais_vendidos = df[df['Faturamento Total (R$)'] > q3_totalfat]

print('\n=========== Listagem dos produtos que foram mais faturados =============')
print(f"\n{mais_vendidos.sort_values(by='Faturamento Total (R$)', ascending=True)}")
