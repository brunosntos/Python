import os
os.system("clear")

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
notas = []
soma = 0

for i in range(3):
    nota = float(input(f"Digite sua {i+1}ª nota: "))
    notas.append(nota)
    soma += nota

media = soma / (i + 1)

os.system("clear")

print(f"Nome do aluno: {nome}")
print(f"Idade: {idade}")

for i in range(3):
    print(f"Nota {i+1}: {notas[i]}")
print(f"Média: {round(media, 1)}")

if (media >= 7):
    print("Situação: Aprovado")
elif (media >= 5) and (media < 7):
    print("Situação: Recuperação")
else:
    print("Situação: Reprovado")
print("\n\n")