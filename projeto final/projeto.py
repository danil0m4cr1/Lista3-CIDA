import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sbs

arquivo = 'dados_filtro2.csv'
arquivoLido = pd.read_csv(arquivo, header=0, delimiter=';')
dados = arquivoLido.to_dict('list')

area = []
volume = []
densidade = []
tensao = []

tamanho = len(dados['ID'])
contador = range(tamanho)

for i in contador:
    raio = dados["Diâmetro (mm)"][i]/2.0
    A = np.pi * (raio**2)
    area.append(A)

    h = dados["Altura (mm)"][i]
    vol = A * h
    volume.append(vol)

    massa = dados["Massa (g)"][i]
    den = massa/vol
    densidade.append(den)

    resistencia = dados["Resistência (kgf)"][i]
    t = resistencia/A
    tensao.append(t)

tensao_media = np.mean(tensao)
tensao_desvio = np.std(tensao)

id_ruins = []

for i in contador:
    valor = tensao[i]
    if valor < 2.67:
        id = dados["ID"][i]
        id_ruins.append(id)

matriz_pearson = [dados["Resistência (kgf)"],
                  dados["Massa (g)"],
                  densidade,
                  dados["Diâmetro (mm)"],
                  area,
                  dados["Altura (mm)"]]
rotulos = ["Resist.", "Massa", "Densidade", "Diâmetro", "Área", "Altura"]

correlacao = np.corrcoef(matriz_pearson)

print(correlacao)

sbs.heatmap(correlacao, annot=True, xticklabels=rotulos, yticklabels=rotulos)
plt.show()

plt.scatter(dados["Diâmetro (mm)"], dados["Resistência (kgf)"])
plt.title("Gráfico da resistência x diâmetro")
plt.show()

# print("Áreas: ", area)
# print("Tensões: ", tensao)
# print("Tensão média: ", tensao_media)
# print("Tensão desvio: ", tensao_desvio)
# print("Outliers: ", id_ruins)

# plt.boxplot(dados["Massa (g)"])
# plt.title("Boxplot da massa")
# plt.show()
#
# plt.boxplot(dados["Resistência (kgf)"])
# plt.title("Boxplot da resistência")
# plt.show()
#
# plt.boxplot(densidade)
# plt.title("Boxplot da densidade")
# plt.show()
#
# plt.boxplot(tensao)
# plt.title("Boxplot da tensão")
# plt.show()
#

