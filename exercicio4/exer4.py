import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

arquivo = "dados4.csv"
arquivo_leitura = pd.read_csv(arquivo, header=0, delimiter=",")
dados = arquivo_leitura.to_dict("list")

b = c = d = m = 0
indB = []
indD = []
indM = []

while c < len(dados["Educacao"]):
    if dados["Educacao"][c] == 'Bacharel':
        indB.append(c)
        b += 1
    if dados["Educacao"][c] == 'Doutorado':
        indD.append(c)
        d += 1
    if dados["Educacao"][c] == 'Mestrado':
        indM.append(c)
        m += 1
    c += 1

salariosBac = []
salariosDout = []
salariosMest = []
for i in indB:
    salariosBac.append(dados["Salario"][i])

for i in indD:
    salariosDout.append(dados["Salario"][i])

for i in indM:
    salariosMest.append(dados["Salario"][i])

plt.boxplot([salariosBac, salariosDout, salariosMest], tick_labels=["Salários Bacharel", "Salários Doutorado", "Salários Mestrado"])
plt.title("Boxplots Salário x Formação")
plt.ylabel("Salários")
plt.show()

print("A) A concentração de pessoas que possui formação em Doutorado, é maior do que o restante das formações\n")

ComGesBac = []
ComGesDout = []
ComGesMest = []
SemGesBac = []
SemGesDout = []
SemGesMest = []
SalCGB = []
SalCGD = []
SalCGM = []
SalSGB = []
SalSGD = []
SalSGM = []

for i in indB:
    if dados["Gestao"][i] == "Sim":
        ComGesBac.append(i)
    else:
        SemGesBac.append(i)

for i in indD:
    if dados["Gestao"][i] == "Sim":
        ComGesDout.append(i)
    else:
        SemGesDout.append(i)

for i in indM:
    if dados["Gestao"][i] == "Sim":
        ComGesMest.append(i)
    else:
        SemGesMest.append(i)

for i in ComGesBac:
    SalCGB.append(dados["Salario"][i])

for i in ComGesDout:
    SalCGD.append(dados["Salario"][i])

for i in ComGesMest:
    SalCGM.append(dados["Salario"][i])

for i in SemGesBac:
    SalSGB.append(dados["Salario"][i])

for i in SemGesDout:
    SalSGD.append(dados["Salario"][i])

for i in SemGesMest:
    SalSGM.append(dados["Salario"][i])

plt.boxplot([SalCGB, SalCGD, SalCGM, SalSGB, SalSGD, SalSGM], tick_labels=["Com Gestão Bacharel",
                                                                           "Com Gestão Doutorado", 
                                                                           "Com Gestão Mestrado",
                                                                           "Sem Gestão Bacharel",
                                                                           "Sem Gestão Doutorado",
                                                                           "Sem Gestão Mestrado"])
plt.title("Boxplot Salários x Educação x Gestão")
plt.ylabel("Salários")
plt.show()

print("B) O cargo de gestão fez com que todas as formações subissem seus salários consideravelmente.\n" \
"Tendo em vista as formações com cargos de gestão, vemos que a formação de mestrado é a que possui maiores salários")