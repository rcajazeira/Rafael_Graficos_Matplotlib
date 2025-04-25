import matplotlib.pyplot as plt

# link da noticia 
# https://agenciadenoticias.ibge.gov.br/agencia-noticias/2012-agencia-de-noticias/noticias/41901-censo-2022-87-da-populacao-brasileira-vive-em-areas-urbanas

# Definir os dados com base na notícia sobre a distribuição da população brasileira
categorias = ["Áreas Urbanas", "Áreas Rurais"]
percentuais = [87.4, 12.6]
cores = ['lightskyblue', 'lightcoral']
explode = (0.1, 0)  # Destacar a primeira fatia (opcional)

# Criar o gráfico de pizza
plt.pie(percentuais, explode=explode, labels=categorias, colors=cores,
        autopct='%1.1f%%', shadow=True, startangle=140)

# Personalizar o gráfico
plt.title("Distribuição da População Brasileira (Censo 2022)")
plt.axis('equal')  # Garante que o gráfico seja um círculo

# Exibir o gráfico
plt.show()