from os import system

system("clear")
erro = 0

while erro == 0:
    try:
        nomeProduto = input("Digite o nome do produto: ")
        precoUnitario = float(input("Digite o preço do produto: "))
        quantidade = float(input("Digite a quantidade adquirida: "))

        compraTotal = quantidade * precoUnitario
        valorDesconto = 0

        if quantidade < 5:
            valorDesconto = compraTotal * 0.02
        elif (quantidade > 5) and (quantidade <= 10):
            valorDesconto = compraTotal * 0.03
        elif quantidade > 10:
            valorDesconto = compraTotal * 0.05

        totalPagar = compraTotal - valorDesconto

        print("")
        print("=" * 30, "\n")
        print(f"Preço total: {compraTotal}")
        print(f"Valor do desconto: {valorDesconto}")
        print(f"Total a pagar: {totalPagar}")
        print("\n")

        erro = 1
    except:
        system("clear")
        print("=== Digite um valor válido.\n")