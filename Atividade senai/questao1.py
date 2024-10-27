import sys
import math

a = int(input("Digite o valor de 'a': "))
b = int(input("Digite o valor de 'b': "))
c = int(input("Digite o valor de 'c': "))

delta = (b**2) - 4 * a * c

if delta < 0:
    sys.exit("A equação não possui raízes reais.")
    
elif delta == 0:
    x = (-b) / (2 * a)
    print(f"\nA raíz é {x}")

else:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)

    print(f"\nPrimeira raíz: {x1}")
    print(f"Segunda raíz: {x2}")