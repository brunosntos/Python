from os import system

system('clear')

def inflacao(valor):
    if valor < 100:
        return valor + (valor * 0.1)
    else:
        return valor + (valor * 0.2)

valorFinal = inflacao(int(input("Digite um valor: ")))

print(f'\n{valorFinal}')