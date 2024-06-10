'''
adicionar opcoes:
exibir todos os livros
exibir todos os usuarios
excluir um livro
excluir um usuario
'''


import os
import sys
import pandas as pd
from time import sleep

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
    limpar()
    print(f'{separador(10)} Biblioteca Digital {separador(10)}\n')
    print('0. Encerrar o Programa')
    print('1. Adicionar livro à biblioteca')
    print('2. Adicionar novo usuário')
    print('3. Exibir livros disponíveis na biblioteca')
    print('4. Emprestar um livro à um usuário')
    print('5. Devolver um livro à biblioteca')
    print('6. Ver livros emprestados à um usuário')

    opcao = input('\nDigite o índice da opção desejada: ')

    match(opcao):
        case '0':
            limpar()
            sys.exit('Programa encerrado.')
        case '1':
            addLivro()
        case '2':
            addUsuario()
        case '3':
            livroDisponiveis()
        case '4':
            emprestarLivro()
        case '5':
            devolverLivro()
        case '6':
            livrosDeUmUsuario()
        case _:
            print('Opção inválida. Tente novamente.')
            sleep(3)
            menu()


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
        livros.write(f'{titulo},{autor},{ano},default\n')
    
    print(f'\nO novo livro [{titulo}] foi adicionado à biblioteca!')

    if input('\nAdicionar mais um livro? (S / N) -> ').lower() == 's':
        addLivro()
    else:
        menu()
    
def livroDisponiveis():
    limpar()
    print(f'{separador(10)} Exibindo livros disponíveis {separador(10)}\n')

    df = pd.read_csv(arquivoLivros)

    for i in range(len(df)):
        if df.iloc[i]['status'] == 'default':
            print(f"Título: {df.iloc[i]['titulo']}, Autor: {df.iloc[i]['autor']}, Ano: {df.iloc[i]['ano']}")
    
    input('\nPressione [ENTER] parar voltar ao menu. ')
    menu()

def addUsuario():
    limpar()
    print(f'{separador(10)} Adicionando Usuário {separador(10)}\n')
    usuario = input('Nome do usuário: ')

    with open (arquivoUsuarios, 'a') as usuarios:
        usuarios.seek(0,2)
        if usuarios.tell() == 0:
            usuarios.write('usuarios\n')
        usuarios.write(f'{usuario}\n')
    
    print(f'\nO novo usuário [{usuario}] foi adicionado à lista!')

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
        if dflivros.iloc[i]['status'] == 'default':
            print(f"{i}. {dflivros.iloc[i]['titulo']}")

    indiceLivro = int(input('\nDigite o índice do livro que você deseja emprestar: '))

    limpar()
    print(f'{separador(10)} Emprestando um Livro {separador(10)}\n')
    for i in range(len(dfusuarios)):
        print(f"{i}. {dfusuarios.iloc[i]['usuario']}")

    indiceUsuario = int(input('\nAgora, digite o índice do usuário que você deseja emprestar: '))

    with open(arquivoTemp, 'w') as temp:
        temp.write('titulo,autor,ano,status\n')
    with open(arquivoTemp, 'a') as temp:
        for i in range(len(dflivros)):
            if i != indiceLivro:
                temp.write(f"{dflivros.iloc[i]['titulo']},{dflivros.iloc[i]['autor']},{dflivros.iloc[i]['ano']},{dflivros.iloc[i]['status']}\n")
            else:
                temp.write(f"{dflivros.iloc[i]['titulo']},{dflivros.iloc[i]['autor']},{dflivros.iloc[i]['ano']},{dfusuarios.iloc[indiceUsuario]['usuario']}\n")
    
    with open(arquivoLivros, 'w') as livros:
        livros.write('')
    with open(arquivoTemp,'r') as temp:
        for linha in temp:
            titulo, autor, ano, status = linha.strip().split(',')
            with open(arquivoLivros, 'a') as livros:
                livros.write(f"{titulo},{autor},{ano},{status}\n")

    print(f'\nO livro foi emprestado ao usuário!')

    input('\nPressione [ENTER] para voltar ao menu')
    menu()


def devolverLivro():
    limpar()
    print(f'{separador(10)} Devolvendo um livro {separador(10)}\n')

    dflivros = pd.read_csv(arquivoLivros)

    for i in range(len(dflivros)):
        if dflivros.iloc[i]['status'] != 'default':
            print(f"{i}. {dflivros.iloc[i]['titulo']} ({dflivros.iloc[i]['status']})")

    indiceLivro = int(input('\nDigite o índice do livro que será devolvido: '))

    with open(arquivoTemp, 'w') as temp:
        temp.write('titulo,autor,ano,status\n')
    with open(arquivoTemp, 'a') as temp:
        for i in range(len(dflivros)):
            if i != indiceLivro:
                temp.write(f"{dflivros.iloc[i]['titulo']},{dflivros.iloc[i]['autor']},{dflivros.iloc[i]['ano']},{dflivros.iloc[i]['status']}\n")
            else:
                temp.write(f"{dflivros.iloc[i]['titulo']},{dflivros.iloc[i]['autor']},{dflivros.iloc[i]['ano']},default \n")
    
    with open(arquivoLivros, 'w') as livros:
        livros.write('')
    with open(arquivoTemp,'r') as temp:
        for linha in temp:
            titulo, autor, ano, status = linha.strip().split(',')
            with open(arquivoLivros, 'a') as livros:
                livros.write(f"{titulo},{autor},{ano},{status}\n")
    
    print(f'\nO livro foi devolvido à biblioteca!')

    input('\nPressione [ENTER] para voltar ao menu')
    menu()

def livrosDeUmUsuario():
    limpar()
    print(f'{separador(10)} Livros emprestados a um usuário {separador(10)}\n')

    dfusuarios = pd.read_csv(arquivoUsuarios)
    dflivros = pd.read_csv(arquivoLivros)

    print(dfusuarios.to_string(index=False))

    usuario = input('\nDigite o nome do usuário para ver seus livros: ')

    limpar()
    print(f'Livros emprestados à {usuario}:')
    with open(arquivoLivros, 'r') as livros:
        for linha in livros:
            titulo, autor, ano, status = linha.strip().split(',')
            if status == usuario.lower():
                print(f'{titulo}')
    
    input('\nPressione [ENTER] para voltar ao menu')
    menu()

menu()