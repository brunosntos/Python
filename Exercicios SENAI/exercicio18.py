from os import system

lista = []

def cabeçalho():
    system('clear')
    print('=' * 20)
    print(' ' * 6, 'SENAI')
    print('=' * 20)

for i in range(5):
    cabeçalho()
    numero = int(input(f'Digite o {i+1}º número: '))

    if numero < 0:
        numero = 0
    
    lista.append(numero)

system('clear')
print('\nExibindo números da lista: ')
for i in range(len(lista)):
    print(f'{i+1}º: {lista[i]}')
