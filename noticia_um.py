import matplotlib.pyplot as plt

# link da notícia
# https://bandnewstv.uol.com.br/ibge-ipca-15-desacelera-em-marco-e-fecha-em-064/

# Definindo então os dados com base na notícia do IPCA-15
categorias = ["em março" , "em fevereiro", " (Alimentação e Bebidas) em março", " (Transportes) em março"]
variacoes = [0.64, 1.23, 1.09, 0.92] # Valores percentuais da notícia [1]

# Criar o gráfico de barras
plt.bar(categorias, variacoes, color=['skyblue', 'lightcoral', 'lightgreen', 'gold'], label="Variação (%)")

# Personalizar o gráfico
plt.title("Variação do IPCA-15 e Grupos em Março de 2025")
plt.xlabel("Índices e Grupos")
plt.ylabel("Variação (%)")
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Adicionar rótulos nas barras para melhor visualização
for i, v in enumerate(variacoes):
    plt.text(i, v + 0.02, str(v) + '%', ha='center', va='bottom')

# Exibir o gráfico
plt.show()