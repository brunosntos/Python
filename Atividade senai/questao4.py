import sys

codigoProduto = int(input("Digite o código do produto (entre 1 e 10): "))

if codigoProduto < 1 or codigoProduto > 10:
    sys.exit("Código de produto inválido.")

pesoProduto = int(input("Digite o peso do produto (kg): "))

codigoPais = int(input("Digite o código do país de origem: "))

if codigoPais < 1 or codigoPais > 3:
    sys.exit("Código de país inválido.")


precoTotal = 0
if codigoProduto >= 1 and codigoProduto <= 4:
    precoTotal = (pesoProduto * 1000) / 10
elif codigoProduto >= 5 and codigoProduto <= 7:
    precoTotal = (pesoProduto * 1000) / 25
elif codigoProduto >= 8 and codigoProduto <= 10:
    precoTotal = (pesoProduto * 1000) / 35


imposto = 0
if codigoPais == 1:
    imposto = precoTotal * 0
elif codigoPais == 2:
    imposto = precoTotal * 0.15
elif codigoPais == 3:
    imposto = precoTotal * 0.25

valorTotal = precoTotal + imposto

print("\n=== EXIBINDO DADOS ===")
print(f"Peso do produto em gramas = {pesoProduto * 1000}g")
print(f"Preço total = R${precoTotal}")
print(f"Valor do imposto = R${imposto}")
print(f"Valor total da compra = R${valorTotal}")