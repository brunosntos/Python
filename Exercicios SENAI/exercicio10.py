from os import system
system("clear")

soma = 0

for i in range(5):
    numero = int(input(f"Digite o {i+1} número: "))
    soma += numero

media = soma / (i+1)

print(f"\nSoma: {soma}")
print(f"Média: {media}")