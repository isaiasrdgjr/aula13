import pandas as pd

data = {
    'Nome': ['Ana', 'João', 'Maria'],
    'Idade': [23, 25, 29],
    'Gênero': ['F', 'M', 'F'],
    'Altura': [1.70, 1.80, 1.75]
}
# print(data)

df_dados = pd.DataFrame(data)
print(df_dados)


# variáveis quantitativas
print('\nExibindo quantitativos: ')
print('Exibindo idade: ')
print(df_dados['Idade'])
print('Exibindo altura:')
print(df_dados['Altura'])

# variáveis qualitativas
print('\nExibindo qualitativos: ')
print('Exibindo nome: ')
print(df_dados['Nome'])
print('Exibindo gênero:')
print(df_dados['Gênero'])
