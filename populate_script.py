import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "setup.settings")
django.setup()

from faker import Faker
from validate_docbr import CPF
import random
from clientes.models import Cliente


def criando_pessoas(quantidade_de_pessoas):
    fake: Faker = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(quantidade_de_pessoas):
        cpf: CPF = CPF()
        nome: str = fake.name()
        email: str = f"{nome.lower()}@{fake.free_email_domain()}"
        email = email.replace(" ", "")
        cpf: str = cpf.generate()
        rg = f"{random.randrange(10, 99)}{random.randrange(100, 999)}" \
             f"{random.randrange(100, 999)}{random.randrange(0, 9)}"
        celular: str = f"{random.randrange(10, 21)} 9{random.randrange(4000, 9999)}-{random.randrange(4000, 9999)}"
        ativo: bool = random.choice([True, False])
        p: Cliente = Cliente(nome=nome, email=email, cpf=cpf, rg=rg, celular=celular, ativo=ativo)
        p.save()

criando_pessoas(50)