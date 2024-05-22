import os
os.system("clear")

continuar = 0

while continuar == 0:
    idade = input("Digite sua idade: ")

    if  not idade.isdigit():
        print("Erro! Você não digitou apenas números.\n")
    else:
        idade = int(idade)
        print("Você não é obrigado a votar!") if (idade < 18) or (idade > 65) else print("Você é obrigado a votar!")
        continuar = 1