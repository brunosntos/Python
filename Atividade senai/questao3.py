altura = int(input("Digite sua altura (cm): "))
peso = float(input("Digite sua altura (kg): "))

tipoPessoa = ""

if altura < 120:
    if peso < 60:
        tipoPessoa = "A"
    elif peso >= 60 and peso <= 90:
        tipoPessoa = "D"
    elif peso > 90:
        tipoPessoa = "G"
elif altura >= 120 and altura <= 170:
    if peso < 60:
        tipoPessoa = "B"
    elif peso >= 60 and peso <= 90:
        tipoPessoa = "E"
    elif peso > 90:
        tipoPessoa = "H"
elif altura > 170:
    if peso < 60:
        tipoPessoa = "C"
    elif peso >= 60 and peso <= 90:
        tipoPessoa = "F"
    elif peso > 90:
        tipoPessoa = "I"

print(f"\nPessoa tipo {tipoPessoa}")
