# =========================================
# Projeto: FarmTech Solutions
# Arquivo: clima_api.R
# Objetivo:
# consultar API meteorológica pública
# e exibir dados climáticos no terminal
# =========================================

# Instale o pacote se for a primeira vez:
# install.packages("jsonlite") # nolint

library(jsonlite)

# Coordenadas aproximadas de São Paulo
latitude <- -23.55
longitude <- -46.63

# Montando a URL da API Open-Meteo
url <- paste0(
  "https://api.open-meteo.com/v1/forecast?latitude=", latitude,
  "&longitude=", longitude,
  "&current=temperature_2m,relative_humidity_2m,wind_speed_10m",
  "&timezone=auto"
)

# Ler JSON da API
dados_clima <- fromJSON(url)

# Mostrar resultados no terminal
cat("=== DADOS METEOROLÓGICOS ATUAIS ===\n")
cat("Temperatura:", dados_clima$current$temperature_2m, "°C\n")
cat("Umidade relativa:", dados_clima$current$relative_humidity_2m, "%\n")
cat("Velocidade do vento:", dados_clima$current$wind_speed_10m, "km/h\n")