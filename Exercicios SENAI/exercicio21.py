from dataclasses import dataclass
import os

os.system('clear')

@dataclass

class Livros():
    titulo: str
    autor: str
    numeroPaginas: int
    preco: int

livros = []

for i in range(2):
    print('Insira os dados do livro:')
    titulo = input('\nTítulo: ')
    autor = input('Autor: ')
    numeroPaginas = input('Número de paginas: ')
    preco = input('Preço: ')
    livro = Livros(titulo = titulo, autor = autor, numeroPaginas = numeroPaginas, preco = preco)
    livros.append(livro)

os.system('clear')

for i,livro in enumerate(livros):
    print(f'Mostrando o Livro: {i+1}')
    print(f'Título: {livro.titulo}')
    print(f'Autor: {livro.autor}')
    print(f'Numero de Páginas: {livro.numeroPaginas}')
    print(f'Preço: {livro.preco}\n')