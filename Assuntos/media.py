import os

os.system("clear")

soma = 0
for i in range(3):
    nota = float(input(f"Digite a nota da unidade {i+1}: "))
    soma += nota

media = soma / 3

print(f"\nMédia: {round(media,1)}\n")

if media >= 5:
    print("Você foi aprovado!")
else:
    print("Você foi reprovado!")
