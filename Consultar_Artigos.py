# %%
import colorama 
from colorama import init, Fore, Style, Back
init(autoreset = True)	

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

# Solicita a cor do artigo
cores = {
    "azul": Fore.BLUE,
    "verde": Fore.GREEN,
    "vermelho": Fore.RED,
    "amarelo": Fore.YELLOW,
    "branco": Fore.WHITE,
    "preto": Fore.BLACK,
    "cinza": Fore.LIGHTBLACK_EX,
    "ciano": Fore.CYAN,
    "magenta": Fore.MAGENTA,
    "laranja": Fore.LIGHTYELLOW_EX,
    "roxo": Fore.LIGHTMAGENTA_EX,
 }

cor = input(" digite a cor do artigo para facilitar a visualização: " ).strip()

if cor in cores:
    cor = cores[cor]
else: 
    print(Fore.RED + Back.BLACK + Style.BRIGHT + "\n Cor inválida. Retornando para a cor padrão.\n")
    cor = Fore.WHITE + Back.BLACK + Style.BRIGHT
    
 # 4. Solicita o número do artigo 
artigo = input(cor + "Digite o número do artigo: ").strip() 


# 5. Procura o artigo
if artigo in artigos["Art."]:
    indice = artigos["Art."].index(artigo)  # Descobre a posição do artigo
    conteudo = artigos["Conteudo"][indice]  # Busca o conteúdo correspondente
    print(cor + f"\n {conteudo} \n")
else:
    print(cor + "\nArtigo não encontrado.\n")
# %%
