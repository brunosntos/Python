from os import system

system('clear')

# método normal

salario = float(input('Digite o salário: '))

if salario < 1500:
    salario += (salario * 0.5)
    print(f'Promoção de 50%.\nTotal = {salario}\n\n')
else:
    salario += (salario * 0.2)
    print(f'Promoção de 20%.\nTotal = {salario}\n\n')

# método walrus

if (salario2:=float(input('Digite o salário: '))) < 1500:
    salario2 += (salario2 * 0.5)
    print(f'Promoção de 50%.\nTotal = {salario2}\n\n')
else:
    salario2 += (salario2 * 0.2)
    print(f'Promoção de 20%.\nTotal = {salario2}\n\n')
