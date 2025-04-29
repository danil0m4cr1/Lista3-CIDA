import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

arquivo = "./dados2.csv"
dados_leitura = pd.read_csv(arquivo, header=0, delimiter=';')
dados = dados_leitura.to_dict('list')

dados["Basquete"].append(0)
dados["Basquete"].append(10)
dados["Basquete"].append(5)
dados["Futebol"].append(2)
dados["Futebol"].append(15)
dados["Futebol"].append(4)

q1Bas = np.percentile(dados["Basquete"], 25, method="averaged_inverted_cdf")
q3Bas = np.percentile(dados["Basquete"], 75, method="averaged_inverted_cdf")
q1Fut = np.percentile(dados["Futebol"], 25, method="averaged_inverted_cdf")
q3Fut = np.percentile(dados["Futebol"], 75, method="averaged_inverted_cdf")

dqBas = q3Bas - q1Bas
vminBas = min(dados["Basquete"])
vmaxBas = max(dados["Basquete"])
dqFut = q3Fut - q1Fut
vminFut = min(dados["Futebol"])
vmaxFut = max(dados["Futebol"])

liBas = max(vminBas, q1Bas - 1.5 * dqBas)
lsBas = min(vmaxBas, q3Bas + 1.5 * dqBas)
liFut = max(vminFut, q1Fut - 1.5 * dqFut)
lsFut = min(vmaxFut, q3Fut + 1.5 * dqFut)

print("Limite inferior Basquete: ", liBas)
print("Limite superior Basquete: ", lsBas)
print("Limite inferior Futebol: ", liFut)
print("Limite superior Futebol: ", lsFut)

mediaBas = np.mean(dados["Basquete"])
mediaFut = np.mean(dados["Futebol"])
medianBas = np.median(dados["Basquete"])
medianFut = np.median(dados["Futebol"])
dpBas = np.std(dados["Basquete"])
dpFut = np.std(dados["Futebol"])

print("\nMédia Basquete: ", round(mediaBas, 2))
print("Mediana Basquete: ", medianBas)
print("Desvio-padrão Basquete: ", round(dpBas, 2))
print("\nMédia Futebol: ", round(mediaFut, 2))
print("Mediana Futebol: ", medianFut)
print("Desvio-padrão Futebol: ", round(dpFut, 2))

plt.boxplot(dados["Basquete"])
plt.title("Boxplot Lesões no Basquete")
plt.ylabel("Lesões")
plt.show()

plt.boxplot(dados["Futebol"])
plt.title("Boxplot Lesões no Futebol")
plt.ylabel("Lesões")
plt.show()

print("D) Como podemos ver, o esporte que possui maior chance de lesões é o Futebol"
      " pois como podemos ver no boxplot, os valores são mais elevados, assim como a média"
      " é superior ao do Basquete")

basquete = []
futebol = []
dados_filtrados = {
   "Basquete": basquete,
   "Futebol": futebol
}

for i in dados["Basquete"]:
    if i > liBas and i < lsBas:
      basquete.append(i)

for i in dados["Futebol"]:
   if i > liFut and i < lsFut:
      futebol.append(i)

mediaNovaBas = np.mean(dados_filtrados["Basquete"])
mediaNovaFut = np.mean(dados_filtrados["Futebol"])
medianaNovaBas = np.median(dados_filtrados["Basquete"])
medianaNovaFut = np.median(dados_filtrados["Futebol"])

print("\nMédia Basquete: ", round(mediaNovaBas, 2))
print("Mediana Basquete: ", round(medianaNovaBas, 2))
print("\nMédia Futebol: ", round(mediaNovaFut, 2))
print("Mediana Futebol: ", round(medianaNovaFut, 2))

plt.boxplot(dados_filtrados["Basquete"])
plt.title("Dados filtrados Basquete")
plt.ylabel("Lesões")
plt.show()

plt.boxplot(dados_filtrados["Futebol"])
plt.title("Dados filtrados Futebol")
plt.ylabel("Lesões")
plt.show()

print("A chance de lesão no Futebol continua sendo maior que a do Basquete")