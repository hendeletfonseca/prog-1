# https://www.beecrowd.com.br/judge/pt/problems/view/1574

for _ in range(int(input())):
    posicao = 0
    instrucoes = []
    for _ in range(int(input())):
        instrucao = input()
        if instrucao == 'LEFT':
            posicao -= 1
        elif instrucao == 'RIGHT':
            posicao += 1
        else:
            gambiarra = ''
            for i in range(8, len(instrucao)):
                gambiarra += instrucao[i]
            instrucao = instrucoes[int(gambiarra) - 1]
            if instrucao == 'LEFT':
                posicao -= 1
            elif instrucao == 'RIGHT':
                posicao += 1
        instrucoes.append(instrucao)
    print(f'{posicao}')
