import os

os.system("clear")

numeros = []

for i in range(5):
    numeros.append(int(input(f"Digite o {i+1}º número: ")))

print(f"\nO maior número digitado foi: {max(numeros)}")
print(f"O menor número digitado foi: {min(numeros)}\n\n")