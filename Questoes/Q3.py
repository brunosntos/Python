numeros = []

for i in range(10):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

print(f"\nNúmeros digitados {numeros}")
print(f"Maior número digitado {max(numeros)}")
print(f"Soma dos números digitados {sum(numeros)}")