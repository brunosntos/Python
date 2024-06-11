import os

os.system('clear')
lista = []

for i in range(5):
    numero = int(input(f'Elemento {i+1}: '))
    lista.append(numero)

print(lista)

print(list(map(lambda x: x*2, lista)))
