from os import system

system("clear")

soma = 0
media = 0

for i in range(4):
    numero = int(input(f"Digite a {i+1}ª nota: "))

    soma += numero

media = soma / (i+1)

print(f"\nMédia: {media}")