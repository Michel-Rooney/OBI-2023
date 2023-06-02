def numero_is_valid(numero):
    if numero < 1 or numero > 500:
        return False
    return True

def numero_consulta_is_valid(index, maximo):
    if index < 1 or index > maximo:
        return False
    return True

def numero_pedido_is_valid(numero):
    if numero < 1 or numero > 1000:
        return False
    return True

numero_tipos, numero_tamanho = input().split()
numero_tipos, numero_tamanho = int(numero_tipos), int(numero_tamanho)
tabela = []


if numero_is_valid(numero_tipos) and numero_is_valid(numero_tamanho):
    for linha in range(numero_tipos):
        tabela.append([])

        valores = input().split()
        if not numero_consulta_is_valid(len(valores), numero_tamanho):
            break

        for coluna in range(numero_tamanho):
            tabela[linha].append(int(valores[coluna]))
    else:
        numero_pedidos = int(input())
        if numero_pedido_is_valid(numero_pedidos):
            total_peca = 0
            for i in range(numero_pedidos):
                index_tipo, index_tamanho = input().split()
                index_tipo, index_tamanho = int(index_tipo), int(index_tamanho)

                if numero_consulta_is_valid(index_tipo, numero_tipos) and numero_consulta_is_valid(index_tamanho, numero_tamanho):
                    peca = tabela[index_tipo -1][index_tamanho -1]
                    if not peca <= 0:
                        total_peca += 1
                        tabela[index_tipo -1][index_tamanho -1] -= 1

            print(total_peca)