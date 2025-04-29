import matplotlib.pyplot as plt
import numpy as np

dados = {
    "Secao": ["Pessoal", "Pessoal", "Pessoal", "Pessoal", "Pessoal", "Pessoal", "Pessoal",
              "Técnica", "Técnica", "Técnica", "Técnica", "Técnica", "Técnica", "Técnica", 
              "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas", "Vendas"],
    "Direito": [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
                9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
    "Politica": [9.0, 6.5, 9.0, 6.0, 6.5, 6.5, 9.0, 6.0, 9.0, 9.0,
                 7.0, 5.5, 6.0, 8.0, 7.0, 9.0, 10.0, 5.5, 7.0, 6.0,
                 6.5, 6.0, 9.0, 6.5, 7.0],
    "Estatistica": [9, 9, 8, 8, 9, 10, 8, 8, 9, 8, 10, 7, 7,
                    9, 8, 7, 8, 9, 2, 7, 7, 8, 9, 8, 7]
}

mediaDir = round(np.mean(dados["Direito"]), 2)
mediaPol = round(np.mean(dados["Politica"]), 2)
mediaEst = round(np.mean(dados["Estatistica"]), 2)
medianaDir = np.median(dados["Direito"])
medianaPol = np.median(dados["Politica"])
medianaEst = np.median(dados["Estatistica"])
dpDir = np.std(dados["Direito"])
dpPol = np.std(dados["Politica"])
dpEst = np.std(dados["Estatistica"])

print("Média Direito: ", mediaDir)
print("Média Política: ", mediaPol)
print("Média Estatística: ", mediaEst)
print("\nMediana Direito: ", medianaDir)
print("Mediana Política: ", medianaPol)
print("Mediana Estatística: ", medianaEst)
print("\nDesvio-padrão Direito: ", dpDir)
print("Desvio-padrão Política: ", round(dpPol, 2))
print("Desvio-padrão Estatística: ", round(dpEst, 2))

plt.boxplot([dados["Direito"], dados["Politica"], dados["Estatistica"]], tick_labels=["Direito", "Política", "Estatística"])
plt.show()

print("B) No boxplot da disciplina Direito, vemos que a concentração de todos os dados se encontra em um único ponto,\n" \
"já os boxplots das disciplinas Política e Estatística seus limites superiores se coincidem, e a concentração dos dados a maior parte se coincidem também,\n" \
"porém, vemos que na Estatística, possui um outlier, sendo ele o número 2.")

c = calc = 0
mediaNotas = []
mediaP = []
mediaT = []
mediaV = []
while c < len(dados["Direito"]):
    calc = dados["Direito"][c] + dados["Politica"][c] + dados["Estatistica"][c]
    media = round((calc/3), 2)
    if dados["Secao"][c] == 'Pessoal':
        mediaP.append(media)

    if dados["Secao"][c] == 'Técnica':
        mediaT.append(media)
    
    if dados["Secao"][c] == 'Vendas':
        mediaV.append(media)

    mediaNotas.append(media)
    
    c += 1

dados["Media"] = mediaNotas

plt.boxplot(dados["Media"])
plt.title("Média Notas Funcionários")
plt.ylabel("Notas")
plt.show()

plt.boxplot([mediaP, mediaT, mediaV, mediaNotas], tick_labels=["Média Pessoal", "Média Técnica", "Média Vendas", "Média Geral"])
plt.title("Boxplot Média x Seção")
plt.ylabel("Notas")
plt.show()

print("D) Podemos identificar que a média da Seção Pessoal, possui uma concentração em resultados mais altos,\n" \
"entretanto seus limites superiores coincidem com todas as seções")