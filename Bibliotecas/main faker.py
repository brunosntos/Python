from faker import Faker
import os

os.system('clear')

faker = Faker('pt-br')

email = faker.email()
numero = faker.msisdn()
cpf = faker.cpf()
cartao = faker.credit_card_number()

print(numero)