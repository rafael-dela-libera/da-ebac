
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Leitura do arquivo CSV
df = pd.read_csv("gasolina.csv")

# Criação do gráfico de linha
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x="dia", y="venda", marker="o")

# Títulos e rótulos
plt.title("Preço da Gasolina por Dia")
plt.xlabel("Dia")
plt.ylabel("Preço (R$)")
plt.grid(True)

# Salvando o gráfico
plt.savefig("gasolina.png")
plt.close()
