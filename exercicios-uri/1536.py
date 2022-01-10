# https://www.beecrowd.com.br/judge/pt/problems/view/1536

def pontuacao(golsA, golsB, saldoA, saldoB):
    if int(golsA) > int(golsB):
        saldoA += 3
    if int(golsA) < int(golsB):
        saldoB += 3
    if int(golsA) == int(golsB):
        saldoA += 1
        saldoB += 1
    return saldoA, saldoB


qtdTestes = int(input())
for _ in range(qtdTestes):
    saldoA, saldoB = 0, 0
    jogo1GolsA, jogo1GolsB = input().split(' x ')
    jogo2GolsB, jogo2GolsA = input().split(' x ')
    saldoA, saldoB = pontuacao(jogo1GolsA, jogo1GolsB, saldoA, saldoB)
    saldoB, saldoA = pontuacao(jogo2GolsB, jogo2GolsA, saldoB, saldoA)
    if saldoA > saldoB:
        print('Time 1')
    if saldoB > saldoA:
        print('Time 2')
    if saldoA == saldoB:
        if (int(jogo1GolsA) + int(jogo2GolsA)) > (int(jogo1GolsB) + int(jogo2GolsB)):
            print('Time 1')
        elif (int(jogo1GolsA) + int(jogo2GolsA)) < (int(jogo1GolsB) + int(jogo2GolsB)):
            print('Time 2')
        elif int(jogo2GolsA) > int(jogo1GolsB):
            print('Time 1')
        elif int(jogo2GolsA) < int(jogo1GolsB):
            print('Time 2')
        else:
            print('Penaltis')
