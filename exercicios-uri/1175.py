# https://www.beecrowd.com.br/judge/pt/problems/view/1175

def construirVetor():
    vetor = []
    for _ in range(20):
        vetor.append(int(input()))
    return vetor


def trocarElementosEImprimir(vetor):
    vetorTemp = []
    for i in range(len(vetor) // 2):
        vetorTemp = vetor[i]
        vetor[i] = vetor[len(vetor) - 1 - i]
        vetor[len(vetor) - 1 - i] = vetorTemp
        print(f'N[{i}] = {vetor[i]}')
    for t in range(len(vetor) // 2, len(vetor)):
        print(f'N[{t}] = {vetor[t]}')
    return


nI = construirVetor()
trocarElementosEImprimir(nI)

