
tabela = []
total_peca_compradas = 0

num_tipos, num_tamanhos = input().split()
num_tipos, num_tamanhos = int(num_tipos), int(num_tamanhos)


for index_tipo in range(num_tipos):
    tabela.append([])

    valores = input().split()
    for index_tamanho in range(num_tamanhos):
        tabela[index_tipo].append(int(valores[index_tamanho]))

num_pedidos = int(input())
for _ in range(num_pedidos):
    index_tipo, index_tamanho = input().split()
    index_tipo, index_tamanho = int(index_tipo), int(index_tamanho)

    peca = tabela[index_tipo -1][index_tamanho -1]
    if peca > 0:
        total_peca_compradas += 1
        tabela[index_tipo -1][index_tamanho -1] -= 1

print(total_peca_compradas)
