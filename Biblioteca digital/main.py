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
arquivoUsuarios = '/workspaces/Python/Biblioteca digital/usuarios.csv'
arquivoTemp = '/workspaces/Python/Biblioteca digital/temp.csv'

if not os.path.exists(arquivoLivros):
    arquivosExists += 1
elif not os.path.exists(arquivoUsuarios):
    arquivosExists += 1
elif not os.path.exists(arquivoTemp):
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
    
    if input('\nAdicionar mais um livro? (S / N) -> ').lower() == 's':
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
    
    input('\nPressione [ENTER] parar voltar ao menu. ')
    menu()

def addUsuario():
    limpar()
    print(f'{separador(10)} Adicionando Usuário {separador(10)}\n')
    nome = input('Nome: ')
    idUser = int(input('ID de usuário: '))

    with open (arquivoUsuarios, 'a') as usuarios:
        usuarios.seek(0,2)
        if usuarios.tell() == 0:
            usuarios.write('nome,iduser\n')
        usuarios.write(f'{nome},{idUser}\n')
    
    if input('\nAdicionar mais um usuário? (S / N) -> ').lower() == 's':
        addUsuario()
    else:
        menu()

def emprestarLivro():
    limpar()
    print(f'{separador(10)} Emprestando um Livro {separador(10)}\n')

    dflivros = pd.read_csv(arquivoLivros)
    dfusuarios = pd.read_csv(arquivoUsuarios)

    for i in range(len(dflivros)):
        if dflivros.iloc[i]['status'] == 0:
            print(f"{i+1}. {dflivros.iloc[i]['titulo']}")

    indiceLivro = int(input('\nDigite o índice do livro que você deseja emprestar: '))

    for i in range(len(dfusuarios)):
        print(f"{i+1}. Usuário: {dfusuarios.iloc[i]['nome']}")

    indiceUsuario = int(input('\nAgora, digite o índice do usuário que você deseja emprestar: '))

    




#addLivro()
#livroDisponiveis()
#ddUsuario()
emprestarLivro()