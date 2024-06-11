from dataclasses import dataclass
import os

QUANTIDADE_ALUNOS = 2

@dataclass
class Aluno():
    nome: str
    idade: int
    peso: float
    altura: float

alunos = []

os.system('clear')

for i in range(QUANTIDADE_ALUNOS):
    nome = input('\nDigite o nome: ')
    idade = int(input('Digite a idade: '))
    peso = float(input('Digite o peso: '))
    altura = float(input('Digite a altura: '))
    aluno = Aluno(nome = nome, idade = idade, peso = peso, altura = altura)
    alunos.append(aluno)

os.system('clear')

for aluno in alunos:
    print(f'Nome: {aluno.nome}')
    print(f'Idade: {aluno.idade}')
    print(f'Peso: {aluno.peso}')
    print(f'Altura: {aluno.altura}\n')
