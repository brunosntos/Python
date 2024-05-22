from os import system

system("clear")
operacao = 1

while (operacao != 0):
    try:
        primeiroNumero = int(input("Digite o valor do primeiro número: "))
        segundoNumero = int(input("Digite o valor do segundo número: "))

        print("\n0. Encerrar o programa")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("")

        operacao = int(input("Escolha a operação a ser exercutada: "))

        system("clear")

        match(operacao):
            case 0:
                print("\nEncerrando...\n")
                break
            case 1:
                print(f"Resultado: {primeiroNumero + segundoNumero}")
            case 2:
                print(f"Resultado: {primeiroNumero - segundoNumero}")
            case 3:
                print(f"Resultado: {primeiroNumero * segundoNumero}")
            case 4:
                print(f"Resultado: {round((primeiroNumero / segundoNumero),1)}")
            case _:
                print("Opção inválida.")
        
        input("\nPressione [ENTER] para continuar ")
        system("clear")
    except:
        system("clear")
        print(">>> O valor inserido é inválido...\n")