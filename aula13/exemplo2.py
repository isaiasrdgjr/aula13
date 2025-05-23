import pandas as pd

df = pd.read_excel('./aula13/vendas_eletronicos.xlsx')

print("\nMaior valor de faturamento: ")
print(df['Faturamento Total (R$)'].max())

print("\nMenor valor de faturamento: ")
print(df['Faturamento Total (R$)'].min())

print("\nSomatório das unidades vendidas: ")
print(df['Unidades Vendidas'].sum())

print("\nMédia dos preços dos produtos: ")
print(df['Preço por Unidade (R$)'].mean())
