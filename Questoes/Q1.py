numeros = []

for i in range(3):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

print(f"\nO maior número digitado foi {max(numeros)}")