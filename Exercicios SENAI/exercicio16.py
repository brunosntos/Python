import os

os.system("clear")

numeros = []
QUANTIDADE = 6
numerosPares = 0
numerosImpares = 0

for i in range(QUANTIDADE):
    numeros.append(float(input(f"Digite o {i+1}º número: ")))

    if numeros[i] % 2 == 0:
        numerosPares += 1
    else:
        numerosImpares += 1

print(f"\nForam digitados {numerosPares} pares.")
print(f"Foram digitados {numerosImpares} ímpares.\n\n")