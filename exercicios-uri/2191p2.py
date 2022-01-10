# https://www.beecrowd.com.br/judge/pt/problems/view/2191

def calcularMaiorSaldo(saldos, n):
    inicio, fim = 1, 1
    maiorSaldo = saldos[0]
    for test in range(n):
        for i in range(n - test):
            saldo = calcularSaldo(i, i + 1 + test, saldos)
            if saldo >= maiorSaldo:
                maiorSaldo = saldo
                inicio = i+1
                fim = i+1+test
                print(maiorSaldo)
    return inicio, fim, maiorSaldo

def calcularSaldo(inicio, final, saldos):
    saldo = 0
    for i in range(inicio, final):
        saldo += saldos[i]
    return saldo


n = int(input())
teste = 1
while n != 0:
    saldos = []
    for _ in range(n):
        x, y = map(int, input().split())
        saldos.append(x-y)
    inicio, fim, saldoFinal = calcularMaiorSaldo(saldos, n)
    print(f'Teste {teste}')
    if saldoFinal > 0:
        print(inicio, fim)
    else:
        print('Nenhum')
    print(saldos)
    n = int(input())
    teste += 1
