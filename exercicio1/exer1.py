import matplotlib.pyplot as plt
import numpy as np

dados = [53.0, 70.2, 84.3, 69.5, 77.8, 87.5, 53.4, 82.5, 67.3, 54.1,
        70.5, 71.4, 95.4, 51.1, 74.4, 55.7, 63.5, 85.8, 53.5, 64.3,
        82.7, 78.5, 55.7, 69.1, 72.3, 59.5, 55.3, 73.0, 52.4, 50.7]

q1 = np.percentile(dados, 25, method="averaged_inverted_cdf")
q3 = np.percentile(dados, 75, method="averaged_inverted_cdf")

dadosB = np.percentile(dados, 95, method="averaged_inverted_cdf")
dadosC = np.percentile(dados, 80, method="averaged_inverted_cdf")

dq = q3 - q1
vmin = min(dados)
vmax = max(dados)

LI = max(vmin, q1 - 1.5 * dq)
LS = min(vmax, q3 + 1.5 * dq)

media = np.mean(dados)
dp = np.std(dados)

dados_filtrados = []
outliers = []
for i in dados:
    if i > (media - dp) and i < (media + dp):
        dados_filtrados.append(i)
    else:
        outliers.append(i)

print("Outliers:")
print(outliers)
print("\nDados Filtrados:")
print(dados_filtrados)
print("\nMédia: ", round(media, 2))
print("Desvio-padrão: ", round(dp, 2))
print("\n95%: ", dadosB)
print("80%: ", dadosC)

plt.boxplot(dados)
plt.title("Box plot dos dados padrões")
plt.ylabel("Dureza")
plt.show()

mediaNova = np.mean(dados_filtrados)
dpNovo = np.std(dados_filtrados)
print("Média nova: ", round(mediaNova, 2))
print("Desvio-padrão novo: ", round(dpNovo, 2))

plt.boxplot(dados_filtrados)
plt.title("Box plot dos dados filtrados")
plt.ylabel("Dureza")
plt.show()