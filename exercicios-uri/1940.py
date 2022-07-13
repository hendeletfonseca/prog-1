jogadores, rodadas = map(int, input().split())
pontuacoes = [] # lista vazia para guardar as pontuações
pontos = list(map(int, input().split())) # recebo os pontos e transformo em uma lista para acessar pelo indice
jogador = 0
maiorValor = 0
maiorIndice = 1

for i in range(jogadores): # crio um novo valor na lista para cada jogador
    pontuacoes.append(0)

for i in pontos: # somo os pontos de cada jogador
    if jogador == len(pontuacoes): # se o jogador ultrapassa o maximo de jogadores volto pro 1º jogador
        jogador = 0
    pontuacoes[jogador] += i
    jogador += 1 # vou pro proximo jogador

for i in range(len(pontuacoes)): # descubro o que tem a maior pontuação
    if pontuacoes[i] >= maiorValor:
        maiorValor = pontuacoes[i]
        maiorIndice = i + 1

print(maiorIndice)