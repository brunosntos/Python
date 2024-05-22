import os

def limpar():
    os.system("clear")

limpar()
nome = input("Digite seu nome: ")
sexo = input("Qual seu sexo? (M / F): ")
estadoCivil = input("Qual seu estado civil? ")

if (sexo.upper() == 'F') and (estadoCivil.upper() == 'CASADA'):
    tempo = input("Há quantos anos você é casada? ")

limpar()

print("=== EXIBINDO RESULTADOS ===\n")
print(f"Nome: {nome}")
print(f"Sexo: {sexo.upper()}")
print(f"Estado Civil: {estadoCivil}")

if (sexo.upper() == 'F') and (estadoCivil.upper() == 'CASADA'):
    print(f"Tempo de casamento: {tempo} anos")
print("")