from classes import Pessoa
from classes import Funcionario
import os

os.system('clear')

pessoasCSV = "/workspaces/Python/Financeiro/pessoas.csv"

pessoas = []
funcionarios = []

pessoas.append(Pessoa('Bruno',19))
funcionarios.append(Funcionario(pessoas[0].nome,pessoas[0].idade,"Junior",2000))

print(pessoas[0].saudacao())
print(funcionarios[0].apresentacao())
print(funcionarios[0].aumentar_salario(1.5))
