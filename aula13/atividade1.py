import numpy as np

dados_casas = [150000 , 180000, 200000, 220000, 250000, 280000, 300000, 320000, 400000, 1500000]

media = np.mean(dados_casas)
mediana = np.median(dados_casas)

print(media, mediana)

print(f'\n O valor mais representativo das vendas é R${mediana}, pois demonstra a realidade da maioria das vendas da imobiliária')
