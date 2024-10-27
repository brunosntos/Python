import os

os.system('clear')

salario_bruto = float(input("Digite o salário bruto: "))

if salario_bruto > 3500:
    salario_liquido = salario_bruto - (salario_bruto * 0.02)
else:
    salario_liquido = salario_bruto + (salario_bruto * 0.01)

print(salario_liquido)  