import sys

x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))
z = int(input("Digite o valor de z: "))

if (x > y + z or y > x + z or z > y + x):
    sys.exit("\nO valor de uma lado não pode ser maior que a soma dos outros dois.")

if (x == y and y == z):
    print("\nTriângulo equilátero")

elif (x == y or y == z or x == z):
    print("\nTriângulo isósceles")

elif (x != y and y != z):
    print("\nTriângulo escaleno")