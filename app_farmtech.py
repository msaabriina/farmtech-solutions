import csv

# Vetores (listas) para guardar os dados
culturas = []
comprimentos = []
larguras = []
areas = []
produtos = []
quantidades = []


# Função para calcular a área do terreno retangular
def calcular_area(comprimento, largura):
    return comprimento * largura


# Função para validar a cultura digitada
def validar_cultura(cultura):
    cultura = cultura.lower().strip()

    if cultura in ["café", "cafe"]:
        return "Café"
    elif cultura in ["cana", "cana-de-açúcar", "cana-de-acucar", "cana de acucar", "cana de açúcar"]:
        return "Cana-de-açúcar"
    else:
        return None


# Função para calcular insumo conforme a cultura
def calcular_insumo(cultura, area):
    if cultura == "Café":
        produto = "Fertilizante fosfatado"
        quantidade = area * 0.25
        unidade = "kg"
        return produto, quantidade, unidade

    elif cultura == "Cana-de-açúcar":
        produto = "Herbicida"
        ruas = int(input("Digite a quantidade de ruas da lavoura: "))
        quantidade = ruas * 0.5
        unidade = "litros"
        return produto, quantidade, unidade


# Função para cadastrar dados
def cadastrar_dados():
    print("\n--- CADASTRO DE LAVOURA ---")

    cultura_digitada = input("Digite a cultura (Café ou Cana-de-açúcar): ")
    cultura = validar_cultura(cultura_digitada)

    if cultura is None:
        print("Cultura inválida. É possível selecionar apenas Café ou Cana-de-açúcar.")
        return

    comprimento = float(input("Digite o comprimento do terreno em metros (ex:1.5): "))
    largura = float(input("Digite a largura do terreno em metros: "))

    area = calcular_area(comprimento, largura)
    produto, quantidade, unidade = calcular_insumo(cultura, area)

    culturas.append(cultura)
    comprimentos.append(comprimento)
    larguras.append(largura)
    areas.append(area)
    produtos.append(produto)
    quantidades.append(f"{quantidade:.2f} {unidade}")

    print("\nDeu tudo certo!! Dados cadastrados com sucesso!")
    print(f"Área calculada: {area:.2f} m²")
    print(f"Insumo necessário: {produto} - {quantidade:.2f} {unidade}")
    print("\nSeus dados estao salvos na memoria do programa, para salvar em um arquivo CSV/Excel, escolha a opcao 5 do menu principal!")


# Função para listar os dados
def listar_dados():
    print("\n--- LISTA DE LAVOURAS ---")

    if len(culturas) == 0:
        print("Ainda não há nenhum dado cadastrado. :( Cadastre uma lavoura para visualizar os dados históricos.")
    else:
        for i in range(len(culturas)):
            print(f"\nRegistro {i}")
            print(f"Cultura: {culturas[i]}")
            print(f"Comprimento: {comprimentos[i]} m")
            print(f"Largura: {larguras[i]} m")
            print(f"Área: {areas[i]:.2f} m²")
            print(f"Produto: {produtos[i]}")
            print(f"Quantidade: {quantidades[i]}")


# Função para atualizar dados em uma posição do vetor
def atualizar_dados():
    print("\n--- ATUALIZAÇÃO DE DADOS ---")

    if len(culturas) == 0:
        print("Não há dados para atualizar. Cadastre uma lavoura para poder atualizar os dados históricos.")
        return

    listar_dados()

    indice = int(input("\nDigite o número do registro que deseja atualizar: "))

    if indice >= 0 and indice < len(culturas):
        cultura_digitada = input("Digite a nova cultura (Café ou Cana-de-açúcar): ")
        nova_cultura = validar_cultura(cultura_digitada)

        if nova_cultura is None:
            print("Cultura inválida. Digite apenas Café ou Cana-de-açúcar, por favor.")
            return

        novo_comprimento = float(input("Digite o novo comprimento em metros (ex:1.5): "))
        nova_largura = float(input("Digite a nova largura em metros (ex:1.5): "))

        nova_area = calcular_area(novo_comprimento, nova_largura)
        novo_produto, nova_quantidade, unidade = calcular_insumo(nova_cultura, nova_area)

        culturas[indice] = nova_cultura
        comprimentos[indice] = novo_comprimento
        larguras[indice] = nova_largura
        areas[indice] = nova_area
        produtos[indice] = novo_produto
        quantidades[indice] = f"{nova_quantidade:.2f} {unidade}"

        print("Registro atualizado com sucesso! Seus dados foram atualizados na memória do programa, para salvar em um arquivo CSV/Excel, escolha a opção 5 do menu principal!")
    else:
        print("Índice inválido.")


# Função para excluir dados
def excluir_dados():
    print("\n--- EXCLUSÃO DE DADOS ---")

    if len(culturas) == 0:
        print("Não há dados para excluir. Cadastre uma lavoura para poder excluir os dados históricos.")
        return

    listar_dados()

    indice = int(input("\nDigite o número do registro que deseja excluir: "))

    if indice >= 0 and indice < len(culturas):
        del culturas[indice]
        del comprimentos[indice]
        del larguras[indice]
        del areas[indice]
        del produtos[indice]
        del quantidades[indice]

        print("Registro excluído com sucesso! Seus dados foram excluídos da memória do programa")
    else:
        print("Índice inválido.")


# Função para salvar os dados em CSV
def salvar_csv():
    with open("dados_lavoura.csv", "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["cultura", "comprimento", "largura", "area", "produto", "quantidade"])

        for i in range(len(culturas)):
            escritor.writerow([
                culturas[i],
                comprimentos[i],
                larguras[i],
                areas[i],
                produtos[i],
                quantidades[i]
            ])

    print("Arquivo foi salvo com sucesso em CSV/Excel. Procure por 'dados_lavoura.csv' no diretório do programa!")


# Menu principal
def menu():
    while True:
        print("\n==============================")
        print("   FARMTECH SOLUTIONS         ")
        print("==============================")
        print("1 - Entrada de dados")
        print("2 - Saída de dados")
        print("3 - Atualização de dados")
        print("4 - Deletar dados")
        print("5 - Salvar dados em CSV/Excel")
        print("6 - Sair do programa")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_dados()
        elif opcao == "2":
            listar_dados()
        elif opcao == "3":
            atualizar_dados()
        elif opcao == "4":
            excluir_dados()
        elif opcao == "5":
            salvar_csv()
        elif opcao == "6":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente. :)")


# Início do programa
menu()
