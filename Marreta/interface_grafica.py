import tkinter as tk
from tkinter import filedialog
from bs4 import BeautifulSoup
import os

def iniciar_troca():
    arquivo_entrada = entry_arquivo_entrada.get()
    nome_livro = entry_nome_livro.get()
    diretorio_saida = entry_diretorio_saida.get()

    # Verificar se os campos obrigatórios foram preenchidos
    if arquivo_entrada == '' or nome_livro == '' or diretorio_saida == '':
        lbl_status.config(text="Por favor, preencha todos os campos.", fg="red")
        return

    # Ler o conteúdo do arquivo HTML de entrada
    with open(arquivo_entrada, 'r', encoding='utf-8') as arquivo:
        conteudoHTML = arquivo.read()

    # Analisar o conteúdo HTML com BeautifulSoup
    soup = BeautifulSoup(conteudoHTML, 'html.parser')

    # Realizar as substituições necessárias
    for secao in soup.find_all('head'):
        # Substituir o nome do livro no HTML
        secao.string.replace_with(nome_livro)

    # Obter o HTML modificado
    novoConteudoHTML = str(soup)

    # Definir o caminho para o arquivo de saída
    nome_arquivo_saida = os.path.basename(arquivo_entrada)
    caminho_arquivo_saida = os.path.join(diretorio_saida, nome_arquivo_saida)

    # Escrever o novo conteúdo no arquivo de saída
    with open(caminho_arquivo_saida, 'w', encoding='utf-8') as arquivo_saida:
        arquivo_saida.write(novoConteudoHTML)

    lbl_status.config(text="Substituição concluída com sucesso.", fg="green")


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
root.title("Marreta Html")

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
