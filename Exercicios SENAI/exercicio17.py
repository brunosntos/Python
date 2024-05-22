import os as a

a.system('clear')

vetor = []
somaPositivos = 0
numerosNegativos = 0

for i in range(10):
    vetor.append(int(input((f'Digite o {i+1}º número: '))))

    if vetor[i] >= 0:
        somaPositivos += vetor[i]
    else:
        numerosNegativos += 1

print(f'\nSoma dos números positivos: {somaPositivos}')
print(f'Quantidade de números negativos: {numerosNegativos}')