# %%
arquivo = "cf88.csv"

# 1. Abre e lê o arquivo
with open(arquivo, "r", encoding="utf-8") as open_file:
    lines = open_file.readlines()

# 2. Processa o cabeçalho (chaves) e inicializa o dicionário
chaves = lines[0].strip("\n").split(";")
artigos = {chave: [] for chave in chaves}

# 3. Lê as linhas seguintes (dados)
for l in lines[1:]:
    valores = l.strip("\n").split(";")
    for i in range(len(valores)):
        artigos[chaves[i]].append(valores[i])

# 4. Solicita o número do artigo
artigo = input("Digite o número do artigo: ").strip()

# 5. Procura o artigo
if artigo in artigos["Art."]:
    indice = artigos["Art."].index(artigo)  # Descobre a posição do artigo
    conteudo = artigos["Conteudo"][indice]  # Busca o conteúdo correspondente
    print(f"\n {conteudo} \n")
else:
    print("\nArtigo não encontrado.\n")
# %%
