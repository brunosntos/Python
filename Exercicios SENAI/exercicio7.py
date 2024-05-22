from os import system
system("clear")

numero = int(input("Digite um valor: "))

for i in range(1, 11):
    print(f"{numero} * {i} = {numero * i}")