numeros = []

for i in range(10):
    numero = float(input("Digite um número: "))
    numeros.append(numero)

media = sum(numeros) / len(numeros)
print(f"\nMédia: {media}")
