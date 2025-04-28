import os
import re

# Caminho da pasta principal
pasta_principal = './'  # <<< ajuste aqui

# Códigos ANSI para colorir
VERMELHO = "\033[31m"
VERDE = "\033[32m"
RESET = "\033[0m"

# Bloco novo do MathJax
novo_bloco_mathjax = """<script>
       window.MathJax = {
         tex: {
           tags: 'ams',
           inlineMath: [['$', '$'], ['\\(', '\\)']],
           macros: {
              bra: ["{\\left\\langle #1 \\right\\rvert}",1],
              ket: ["{\\left\\lvert #1 \\right\\rangle}",1],
              braket:["{\\left\\langle #1 \\vert #2 \\right\\rangle}",2],
              opProj:["{\\left\\lvert #1 \\right\\rangle\\left\\langle #1 \\right\\rvert}",1],
              opUni:["{\\left\\lvert #1 \\right\\rangle\\left\\langle #1 \\right\\rvert \+ \\left\\lvert #2 \\right\\rangle\\left\\langle #2 \\right\\rvert}",2],
              arcsec: "{\\operatorname{arcsec}}",
              arccot: "{\\operatorname{arccot}}",
              arccsc: "{\\operatorname{arcsc}}",
              sech: "{\\operatorname{sech}}",
              csch: "{\\operatorname{csch}}",
              argsinh: "{\\operatorname{arg sinh}}",
              argcosh: "{\\operatorname{arg cosh}}",
              argtanh: "{\\operatorname{arg tanh}}",
              argcoth: "{\\operatorname{arg coth}}",
              argsech: "{\\operatorname{arg sech}}",
              argcsch: "{\\operatorname{arg csch}}",
              dbar: "{\\mathscr'26\\mkern-12mu \\mathrm{d}}"
          }
         }
       };
     </script>"""

# Padrões
padrao_comentario = re.compile(r'^\s*<!--')

padrao_mathjax = re.compile(
    r'(<script[^>]*src="(?P<relativo>(\.\./)+)comunHtml/[^"]*?mathjax[^"]*?[^"]*?"[^>]*></script>)',
    flags=re.IGNORECASE
)

padrao_jquery = re.compile(
    r'(<script[^>]*src="(?P<relativo>(\.\./)+)comunHtml/node_modules/jquery/dist/jquery\.min\.js"[^>]*></script>)',
    flags=re.IGNORECASE
)

padrao_blocos_mathjax = re.compile(
    r'(<script\s+type="text/x-mathjax-config">.*?</script>\s*){2,}',
    flags=re.IGNORECASE | re.DOTALL
)

# Função principal
def processar_arquivo(caminho_arquivo):
    alterado = False
    novas_linhas = []

    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            linhas = f.readlines()
    except UnicodeDecodeError:
        with open(caminho_arquivo, 'r', encoding='latin-1') as f:
            linhas = f.readlines()

    # 1ª Parte: Corrigir MathJax e JQuery nos <script> linha a linha
    for linha in linhas:
        if padrao_comentario.match(linha):
            novas_linhas.append(linha)
            continue

        match_mathjax = padrao_mathjax.search(linha)
        match_jquery = padrao_jquery.search(linha)

        if match_mathjax:
            alterado = True
            relativo = match_mathjax.group('relativo')
            linha_original = linha.strip()
            nova_linha = f'<script src="{relativo}comunHtml/mathjax_new/tex-chtml.js" id="MathJax-script" async></script>'

            print(f"\nArquivo alterado (MathJax): {caminho_arquivo}")
            print(f"{VERMELHO}Linha original:{RESET} {linha_original}")
            print(f"{VERDE}Linha corrigida:{RESET} {nova_linha}")

            novas_linhas.append(f'<!-- {linha_original} -->\n')
            novas_linhas.append(f'{nova_linha}\n')

        elif match_jquery:
            alterado = True
            relativo = match_jquery.group('relativo')
            linha_original = linha.strip()
            nova_linha = f'<script src="{relativo}comunHtml/jquery/dist/jquery.min.js"></script>'

            print(f"\nArquivo alterado (JQuery): {caminho_arquivo}")
            print(f"{VERMELHO}Linha original:{RESET} {linha_original}")
            print(f"{VERDE}Linha corrigida:{RESET} {nova_linha}")

            novas_linhas.append(f'<!-- {linha_original} -->\n')
            novas_linhas.append(f'{nova_linha}\n')

        else:
            novas_linhas.append(linha)

    conteudo_final = ''.join(novas_linhas)

    # 2ª Parte: Corrigir bloco MathJax gigante
    for match in padrao_blocos_mathjax.finditer(conteudo_final):
        trecho_encontrado = match.group(0)

        # Ignora se já comentado
        if '<!--' in trecho_encontrado.splitlines()[0]:
            continue

        conteudo_final = conteudo_final.replace(trecho_encontrado, novo_bloco_mathjax)
        alterado = True

        print(f"\nArquivo alterado (Bloco MathJax): {caminho_arquivo}")
        print(f"{VERMELHO}Trecho original:{RESET}\n{trecho_encontrado.strip()}\n")
        print(f"{VERDE}Trecho novo:{RESET}\n{novo_bloco_mathjax.strip()}\n")

    if alterado:
        try:
            with open(caminho_arquivo, 'w', encoding='utf-8') as f:
                f.write(conteudo_final)
        except UnicodeEncodeError:
            with open(caminho_arquivo, 'w', encoding='latin-1') as f:
                f.write(conteudo_final)

# Percorrer a árvore de diretórios
for dirpath, dirnames, filenames in os.walk(pasta_principal):
    for filename in filenames:
        if filename.endswith('.html') or filename.endswith('.htm'):
            caminho_completo = os.path.join(dirpath, filename)
            processar_arquivo(caminho_completo)
