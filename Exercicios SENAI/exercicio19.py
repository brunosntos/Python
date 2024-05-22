from os import system

system('clear')

def calculos(primeiroNumero,segundoNumero):
    soma = primeiroNumero + segundoNumero
    subtracao = primeiroNumero - segundoNumero
    multiplicacao = primeiroNumero * segundoNumero
    divisao = primeiroNumero / segundoNumero

    return soma, subtracao, multiplicacao, divisao

numero1 = int(input('Digite o primeiro valor: '))
numero2 = int(input('Digite o segundo valor: '))

soma, subtracao, multiplicacao, divisao = calculos(numero1,numero2)

print(f'\n{soma} \n{subtracao} \n{multiplicacao} \n{divisao}\n\n')