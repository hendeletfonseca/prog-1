# https://www.beecrowd.com.br/judge/pt/problems/view/2449

movimentos = 0
listaComparacao = []
aux = 0
qtdPinos, altura = map(int, input().split())
alturaPinos = input().split()
alturaPinos = [int(x) for x in alturaPinos]
for _ in range(qtdPinos):
    listaComparacao.append(altura)
while alturaPinos != listaComparacao:
    while alturaPinos[aux] != altura:
        if alturaPinos[aux] < altura:
            alturaPinos[aux] += 1
            alturaPinos[aux + 1] += 1
            movimentos += 1
        if alturaPinos[aux] > altura:
            alturaPinos[aux] -= 1
            alturaPinos[aux + 1] -= 1
            movimentos += 1
    aux += 1
print(movimentos)
