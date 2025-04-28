import os
import re

# Caminho da pasta principal
pasta_principal = './'  # <<< ajuste aqui

# Códigos ANSI para colorir
VERMELHO = "\033[31m"
VERDE = "\033[32m"
RESET = "\033[0m"

# Expressão regular: captura href="caminho" ou src="caminho"
padrao_relativo = re.compile(
    r'(href|src)="(\.\./\.\./\.\./[^"]*)"',  # pega até fechar a aspa
    flags=re.IGNORECASE
)

def processar_arquivo(caminho_arquivo):
    alterado = False

    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            conteudo = f.read()
    except UnicodeDecodeError:
        with open(caminho_arquivo, 'r', encoding='latin-1') as f:
            conteudo = f.read()

    # Função para substituir as ocorrências
    def substituir(match):
        atributo = match.group(1)
        caminho = match.group(2)
        novo_caminho = caminho.replace('../../../', '../../../../', 1)  # troca só no começo
        print(f"\nArquivo alterado: {caminho_arquivo}")
        print(f"{VERMELHO}Original:{RESET} {atributo}=\"{caminho}\"")
        print(f"{VERDE}Corrigido:{RESET} {atributo}=\"{novo_caminho}\"")
        return f'{atributo}="{novo_caminho}"'

    # Aplicar substituição
    conteudo_novo, num_substituicoes = padrao_relativo.subn(substituir, conteudo)

    if num_substituicoes > 0:
        alterado = True

    if alterado:
        try:
            with open(caminho_arquivo, 'w', encoding='utf-8') as f:
                f.write(conteudo_novo)
        except UnicodeEncodeError:
            with open(caminho_arquivo, 'w', encoding='latin-1') as f:
                f.write(conteudo_novo)

# Percorrer a árvore de diretórios
for dirpath, dirnames, filenames in os.walk(pasta_principal):
    for filename in filenames:
        if filename.endswith('.html') or filename.endswith('.htm'):
            caminho_completo = os.path.join(dirpath, filename)
            processar_arquivo(caminho_completo)
