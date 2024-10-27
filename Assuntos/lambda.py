import os

os.system('clear')

calcular_imposto = lambda x: x + (x * 0.5)

lista_precos = [10,30,50]
lista_precos_atualizados = list(map(lambda x: x + (x * 0.5), lista_precos))

print(lista_precos_atualizados)
