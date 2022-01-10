# https://www.beecrowd.com.br/judge/pt/problems/view/2191

def calcularMaiorSaldo(saldos):
    inicio, fim = 1, 1
    maiorSaldo = saldos[0]
    for i in range(len(saldos)):
        saldo = calcularSaldo(i, i+1, saldos)
        if saldo >= maiorSaldo:
            maiorSaldo = saldo
            inicio, fim = i+1, i+1
    for i in range(len(saldos)-1):
        saldo = calcularSaldo(i, i+2, saldos)
        if saldo >= maiorSaldo:
            maiorSaldo = saldo
            inicio, fim = i+1, i+2
    for i in range(len(saldos)-2):
        saldo = calcularSaldo(i, i+3, saldos)
        if saldo >= maiorSaldo:
            maiorSaldo = saldo
            inicio, fim = i+1, i+3
    for i in range(len(saldos)-3):
        saldo = calcularSaldo(i, i+4, saldos)
        if saldo >= maiorSaldo:
            maiorSaldo = saldo
            inicio, fim = i + 1, i + 4
    for i in range(len(saldos)-4):
        saldo = calcularSaldo(i, i+5, saldos)
        if saldo >= maiorSaldo:
            maiorSaldo = saldo
            inicio, fim = i + 1, i + 5
    for i in range(len(saldos)-5):
        saldo = calcularSaldo(i, i+6, saldos)
        if saldo >= maiorSaldo:
            maiorSaldo = saldo
            inicio, fim = i + 1, i + 6
    for i in range(len(saldos)-6):
        saldo = calcularSaldo(i, i+7, saldos)
        if saldo >= maiorSaldo:
            maiorSaldo = saldo
            inicio, fim = i + 1, i + 7
    for i in range(len(saldos)-7):
        saldo = calcularSaldo(i, i+8, saldos)
        if saldo >= maiorSaldo:
            maiorSaldo = saldo
            inicio, fim = i + 1, i + 8
    for i in range(len(saldos)-8):
        saldo = calcularSaldo(i, i+9, saldos)
        if saldo >= maiorSaldo:
            maiorSaldo = saldo
            inicio, fim = i + 1, i + 9
    return inicio, fim

def calcularSaldo(inicio, final, saldos):
    saldo = 0
    for i in range(inicio, final):
        saldo += saldos[i]
    return saldo


saldos = []
n = int(input())
while n != 0:
    for _ in range(n):
        x, y = map(int, input().split())
        saldos.append(x-y)
    inicio, fim = calcularMaiorSaldo(saldos)
    print(inicio, fim)
    n = int(input())