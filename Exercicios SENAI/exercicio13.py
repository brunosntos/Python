from os import system

system("clear")

soma = 0

for i in range(3):
    numero = float(input(f"Digite a {i+1}ª nota: "))
    soma += numero

media = soma / (i+1)

print(f"\nMédia: {round(media,1)}")

if media >= 7:
    print("Situação: Aprovado")
elif (media >= 4) and (media < 7):
    print("Situação: Recuperação")
elif media < 4:
    print("Situação: Reprovado")