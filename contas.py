
def valor_disponivel_is_valid(valor):
    if valor < 0 or valor > 2000:
        return False
    return True

def valor_conta_is_valid(valor):
    if valor < 1 or valor > 1000:
        return False
    return True


valor_disponivel = int(input())
conta_acougue =  int(input())
conta_farmacia = int(input())
conta_padaria = int(input())
maior_numero_contas = 0

if not valor_disponivel_is_valid(valor_disponivel):
    pass
elif not valor_conta_is_valid(conta_acougue):
    pass
elif not valor_conta_is_valid(conta_farmacia):
    pass
elif not valor_conta_is_valid(conta_padaria):
    pass
else:
    if (conta_acougue + conta_farmacia + conta_padaria) <= valor_disponivel:
        maior_numero_contas = 3
    elif (conta_acougue + conta_farmacia) <= valor_disponivel or \
         (conta_acougue + conta_padaria) <= valor_disponivel or \
         (conta_farmacia + conta_padaria) <= valor_disponivel:
        maior_numero_contas = 2
    elif (conta_acougue) <= valor_disponivel or \
         (conta_farmacia) <= valor_disponivel or \
         (conta_padaria) <= valor_disponivel:
        maior_numero_contas = 1

print(maior_numero_contas)

