import os
import sys
import pandas as pd

def limpar():
    os.system('clear')

def separador(quantidade):
    return '=' * quantidade

limpar()

arquivosExists = 0
arquivoLivros = '/workspaces/Python/Biblioteca digital/livros.csv'

if not os.path.exists(arquivoLivros):
    arquivosExists += 1

if arquivosExists != 0:
    sys.exit('Programa encerrado por falta de arquivos.\n\n')

def menu():
    print('menu')

def addLivro():
    limpar()
    print(f'{separador(10)} Adicionando Livro {separador(10)}\n')
    titulo = input('Título: ').strip()
    autor = input('Autor: ').strip()
    ano = input('Ano: ').strip()

    with open(arquivoLivros, 'a') as livros:
        livros.seek(0,2)
        if livros.tell() == 0:
            livros.write('titulo,autor,ano,status\n')
        livros.write(f'{titulo},{autor},{ano},0\n')
    
    if input('\nAdicionar mais um livro? (S / N) ').lower() == 's':
        addLivro()
    else:
        menu()
    
def livroDisponiveis():
    limpar()
    print(f'{separador(10)} Exibindo livros disponíveis {separador(10)}\n')

    df = pd.read_csv(arquivoLivros)

    for i in range(len(df)):
        if df.iloc[i]['status'] == 0:
            print(f"Título: {df.iloc[i]['titulo']}, Autor: {df.iloc[i]['autor']}, Ano: {df.iloc[i]['ano']}")

addLivro()
livroDisponiveis()