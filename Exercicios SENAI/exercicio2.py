import os
os.system("clear")

numeroUm = int(input("Digite o primeiro número: "))
numeroDois = int(input("Digite o segundo número: "))

soma = numeroUm + numeroDois
media = soma / 2
produto = numeroUm * numeroDois

print("")
print(f"Soma: {soma}")
print(f"Média: {media}")
print(f"Produto: {produto}")
if numeroUm > numeroDois:
    print(f"Maior valor: {numeroUm}")
    print(f"Menor valor: {numeroDois}")
elif numeroDois > numeroUm:
    print(f"Maior valor: {numeroDois}")
    print(f"Menor valor: {numeroUm}")
else:
    print("Os números são iguais!")
print("\n\n")