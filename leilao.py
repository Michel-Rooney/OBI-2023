import string


def num_lances_is_valid(num):
    if num < 0 or num > 10_000:
        return False
    return True

def existe_acento_nome(nome):
    for letra in nome:
        if letra not in string.ascii_letters:
            return True
    return False

def tamanho_nome_is_valid(nome):
    if len(nome) < 1 or len(nome) > 10:
        return False
    return True

def valor_is_valid(valor):
    if valor < 1 or valor > 100_000:
        return False
    return True


maior_lance = 0
pessoa_ganhadora = ''
num_lances = int(input())

if num_lances_is_valid(num_lances):
    for _ in range(num_lances):
        nome = str(input())

        if not tamanho_nome_is_valid(nome):
            break

        if existe_acento_nome(nome):
            break

        valor = int(input())

        if not valor_is_valid(valor):
            break

        if valor > maior_lance:
            pessoa_ganhadora = nome
            maior_lance = valor
    else:
        print(pessoa_ganhadora)
        print(maior_lance)