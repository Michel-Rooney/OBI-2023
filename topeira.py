

num_saloes, num_tuneis = map(int, input().split())
morro = {}
caminhos = []

for sala in range(num_saloes):
    morro[sala + 1] = set()

for tunel in range(num_tuneis):
    sala1, sala2 = map(int, input().split())
    
    morro[sala1].add(sala2)
    morro[sala2].add(sala1)

susgestoes = int(input())
sugestoes_validas = 0
caminho_possivel = False

for sugestao in range(susgestoes):
    caminhos.append(list(map(int, input().split())))

for caminho in range(len(caminhos)):
    for index_salao in range(len(caminhos[caminho])):
        if index_salao == 0:
            continue

        if index_salao == len(caminhos[caminho]) -1:
            break

        if caminhos[caminho][index_salao + 1] in list(morro[caminhos[caminho][index_salao]]):
            caminho_possivel = True
        else:
            caminho_possivel = False
            break
    
    if caminho_possivel:
        sugestoes_validas += 1

    caminho_possivel = False

print(sugestoes_validas)
