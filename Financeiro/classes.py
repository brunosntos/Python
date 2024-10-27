class Pessoa():
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        return f"Olá {self.nome}! ({self.idade} anos)"
    
class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, salario):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.salario = salario

    def apresentacao(self):
        return f"Olá {self.nome}! - {self.idade} anos; Cargo: {self.cargo}; Salário: R${self.salario}"
    
    def aumentar_salario(self, percentual):
        return f"Aumento de R${self.salario * percentual}. Total atualizado: R${self.salario + (self.salario * percentual)}"

