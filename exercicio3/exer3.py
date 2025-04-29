import matplotlib.pyplot as plt
import numpy as np

dados = {
    "Alunas": [154, 109, 137, 115, 152, 140, 154, 178, 101,
               103, 126, 126, 137, 165, 165, 129, 200, 148],
    "Alunos": [108, 140, 114, 91, 180, 115, 126, 92, 169, 146,
               109, 132, 75, 88, 113, 151, 70, 115, 187, 104]
}

mediaAlunas = np.mean(dados["Alunas"])
medianaAlunas = np.median(dados["Alunas"])
mediaAlunos = np.mean(dados["Alunos"])
medianaAlunos = np.median(dados["Alunos"])

print("Média Alunas: ", round(mediaAlunas, 2))
print("Mediana Alunas: ", medianaAlunas)
print("\nMédia Alunos: ", round(mediaAlunos, 2))
print("Mediana Alunos: ", medianaAlunos)
print("\nA) Pois os dados estão distribuidos entre um mínimo e um máximo muito distantes")

plt.boxplot(dados["Alunas"])
plt.title("Dados Notas Alunas")
plt.ylabel("Notas")
plt.show()

q1Alunas = np.percentile(dados["Alunas"], 25, method="averaged_inverted_cdf")
q3Alunas = np.percentile(dados["Alunas"], 75, method="averaged_inverted_cdf")

dqAlunas = q3Alunas - q1Alunas
vminAlunas = min(dados["Alunas"])
vmaxAlunas = max(dados["Alunas"])

liAlunas = max(vminAlunas, q1Alunas - 1.5 * dqAlunas)
lsAlunas = min(vmaxAlunas, q3Alunas + 1.5 * dqAlunas)

dadosFiltAlunas = []

for i in dados["Alunas"]:
    if i > liAlunas and i < lsAlunas:
        dadosFiltAlunas.append(i)

mediaFiltrada = round(np.mean(dadosFiltAlunas), 2)
medianaFiltrada = np.median(dadosFiltAlunas)

print("\nMédia Filtrada: ", mediaFiltrada)
print("Mediana Filtrada: ", medianaFiltrada)

plt.boxplot(dadosFiltAlunas)
plt.title("Dados Filtrados Alunas")
plt.ylabel("Notas")
plt.show()

plt.boxplot([dados["Alunas"], dados["Alunos"]], tick_labels=["Alunas", "Alunos"])
plt.title("Boxplot de comparação de notas")
plt.ylabel("Notas")
plt.show()

print("Possui uma maior concentração de notas maiores no grupo de Alunas, contendo um outlier ainda por cima, em seu grupo." \
"\nJá o grupo de Alunos, está distribuído entre um Limite Inferior e Limite Superior, muito maior que o grupo de Alunas, porém sua concentração continua sendo menor")