# =========================================
# Projeto: FarmTech Solutions
# Arquivo: estatistica_farmtech.R
# Objetivo:
# ler os dados do CSV e calcular média
# e desvio padrão da área plantada
# =========================================

# Ler o arquivo CSV gerado pelo Python
dados <- read.csv("dados_lavoura.csv", stringsAsFactors = FALSE)

# Mostrar os dados
print("Dados carregados:")
print(dados)

# Calcular média da área
media_area <- mean(dados$area)

# Calcular desvio padrão da área
desvio_area <- sd(dados$area)

# Mostrar resultados
cat("\nMédia da área plantada:", media_area, "m²\n")
cat("Desvio padrão da área plantada:", desvio_area, "m²\n")

# Média por cultura
media_por_cultura <- aggregate(area ~ cultura, data = dados, mean)

cat("\nMédia da área por cultura:\n")
print(media_por_cultura)