import re
from validate_docbr import CPF

def cpf_valido(numero_cpf):
    cpf = CPF()
    return cpf.validate(numero_cpf)


def nome_valido(nome_cliente):
    return nome_cliente.isalpha()


def rg_valido(rg_cliente):
    return len(rg_cliente) == 9


def celular_valido(celular_cliente):
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, celular_cliente)
    return resposta
