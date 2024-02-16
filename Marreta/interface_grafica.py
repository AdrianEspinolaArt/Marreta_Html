import tkinter as tk
from tkinter import filedialog
import os
import re

def iniciar_troca():
    arquivo_entrada = entry_arquivo_entrada.get()
    diretorio_saida = entry_diretorio_saida.get()
    nome_livro = entry_nome_livro.get()

    # Verificar se os campos obrigatórios foram preenchidos
    if arquivo_entrada == '' or diretorio_saida == '' or nome_livro == '':
        lbl_status.config(text="Por favor, preencha todos os campos.", fg="red")
        return

    try:
        # Ler o conteúdo do arquivo HTML de entrada
        with open(arquivo_entrada, 'r', encoding='utf-8') as arquivo:
            conteudoHTML = arquivo.read()

        # Encontrar as seções delimitadas pelas tags <inicio_sec> e </inicio_sec>
        secoes = re.findall(r'<inicio_sec> inicio</inicio_sec>(.*?)<inicio_sec> fim</inicio_sec>', conteudoHTML, re.DOTALL)

        # Ler o cabeçalho para a primeira seção
        with open('header_cap.txt', 'r', encoding='utf-8') as header_file:
            cabecalho_cap = header_file.read()

        # Substituir o nome do livro no cabeçalho
        cabecalho_cap = cabecalho_cap.replace('(NOME DO LIVRO)', nome_livro)

        # Ler o cabeçalho para as seções subsequentes
        with open('header_sec.txt', 'r', encoding='utf-8') as header_file:
            cabecalho_sec = header_file.read()

        # Substituir o nome do livro no cabeçalho
        cabecalho_sec = cabecalho_sec.replace('(NOME DO LIVRO)', nome_livro)

        # Ler o rodapé
        with open('rodape.txt', 'r', encoding='utf-8') as rodape_file:
            rodape = rodape_file.read()

        # Gravar cada seção em um arquivo separado
        for i, secao in enumerate(secoes):
            # Obter o conteúdo do h2 para esta seção
            h2_match = re.search(r'<h2[^>]*>(.*?)</h2>', secao, re.IGNORECASE)
            if h2_match:
                nome_secao = h2_match.group(1)
            else:
                nome_secao = f'Seção {i+1}'

            # Escolher o cabeçalho apropriado para esta seção
            if i == 0:
                cabecalho = cabecalho_cap
            else:
                cabecalho = cabecalho_sec

            # Substituir o campo 'nome_secao' no cabeçalho da seção
            cabecalho = cabecalho.replace('(conteudo do h2)', nome_secao)

            # Definir o caminho para o arquivo de saída
            nome_arquivo_saida = f'secao_{i+1}.html'
            caminho_arquivo_saida = os.path.join(diretorio_saida, nome_arquivo_saida)

            # Adicionar o rodapé ao final da seção
            secao_completa = cabecalho + secao + rodape

            # Escrever a seção no arquivo de saída
            with open(caminho_arquivo_saida, 'w', encoding='utf-8') as arquivo_saida:
                arquivo_saida.write(secao_completa)

        lbl_status.config(text="Divisão em seções concluída com sucesso.", fg="green")

    except Exception as e:
        lbl_status.config(text=str(e), fg="red")


def selecionar_arquivo():
    arquivo = filedialog.askopenfilename(filetypes=[("Arquivos HTML", "*.html")])
    entry_arquivo_entrada.delete(0, tk.END)
    entry_arquivo_entrada.insert(0, arquivo)

def selecionar_diretorio():
    diretorio = filedialog.askdirectory()
    entry_diretorio_saida.delete(0, tk.END)
    entry_diretorio_saida.insert(0, diretorio)


# Criar a janela principal
root = tk.Tk()
root.title("Marreta HTML")

# Criar e posicionar os widgets
lbl_arquivo_entrada = tk.Label(root, text="Arquivo HTML de Entrada:")
lbl_arquivo_entrada.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

entry_arquivo_entrada = tk.Entry(root, width=50)
entry_arquivo_entrada.grid(row=0, column=1, padx=5, pady=5)

btn_selecionar_arquivo = tk.Button(root, text="Selecionar Arquivo", command=selecionar_arquivo)
btn_selecionar_arquivo.grid(row=0, column=2, padx=5, pady=5)

lbl_nome_livro = tk.Label(root, text="Nome do Livro:")
lbl_nome_livro.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

entry_nome_livro = tk.Entry(root, width=50)
entry_nome_livro.grid(row=1, column=1, padx=5, pady=5)

lbl_diretorio_saida = tk.Label(root, text="Diretório de Saída:")
lbl_diretorio_saida.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)

entry_diretorio_saida = tk.Entry(root, width=50)
entry_diretorio_saida.grid(row=2, column=1, padx=5, pady=5)

btn_selecionar_diretorio = tk.Button(root, text="Selecionar Diretório", command=selecionar_diretorio)
btn_selecionar_diretorio.grid(row=2, column=2, padx=5, pady=5)

btn_iniciar_troca = tk.Button(root, text="Iniciar Marreta", command=iniciar_troca)
btn_iniciar_troca.grid(row=3, column=1, padx=5, pady=5)

lbl_status = tk.Label(root, text="", fg="black")
lbl_status.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

# Executar o loop principal da aplicação
root.mainloop()