from os import system

system("clear")

notas = []
soma = 0

for i in range(3):
    notas.append(float(input(f"Digite a {i+1}ª nota: ")))
    soma += notas[i]

media = soma / (i+1)

print(f"\nMédia das notas: {round(media,1)}")
print("\nNotas inseridas: \n")

i = 0
for nota in notas:
    i += 1
    print(f"{i}ª: {nota}")