soma = 0

while True:
    numero = int(input("Digite um número: "))

    if numero == 0:
        break

    soma += numero

print(f"\nA soma dos número é {soma}")