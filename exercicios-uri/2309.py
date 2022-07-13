sequencia = [4, 5, 6, 7, 12, 11, 13, 1, 2, 3] #criei uma lista que mostra a ordem de "força" de cada carta (tirado do texto)
vitoriasA = 0 # total de vitorias do jogador A
vitoriasB = 0

testes = int(input()) # recebo quantas partidas vão acontecer 

for i in range(testes):
    a1,a2,a3,b1,b2,b3 = map(int,input().split()) # recebo quais cartas foram jogadas na partida
    pontuacaoA = 0 # quantas vitórias na rodada o jogador teve
    pontuacaoB = 0

    if sequencia.index(a1) >= sequencia.index(b1):
        pontuacaoA += 1
    else:
        pontuacaoB += 1
    
    if sequencia.index(a2) >= sequencia.index(b2):
        pontuacaoA += 1
    else:
        pontuacaoB += 1

    if sequencia.index(a3) >= sequencia.index(b3):
        pontuacaoA += 1
    else:
        pontuacaoB += 1

    '''
    Nessa sequência de if's e else's eu uso a função index(), ela retorna a posição do parametro dentro da lista,
    nesse caso vai pegar o elemento a1,a2,a3... e vai procurar eles dentro da lista sequencia, retornando a posição,
    como a lista sequencia foi ordenada na ordem de "força" das cartas quanto maior o indice  mais forte a carta.

    exemplo: se a1 = 3 e b1 = 7 sequencia.index(a1) vai retornar 9 - porque o 3 é o ultimo elemento da lista
    e sequencia.index(b1) vai retornar 3 já que é o 4° termo (lembrando que indice de lista inicia em 0)
    '''

    if pontuacaoA > pontuacaoB: # aqui vejo quem pontuou mais naquela partida e somo uma vitória 
        vitoriasA += 1
    else:
        vitoriasB += 1

print(f"{vitoriasA} {vitoriasB}")
