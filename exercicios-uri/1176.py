# https://www.beecrowd.com.br/judge/pt/problems/view/1176

def construirFib():
    fibonacci = [0, 1]
    for i in range(2, 61):
        fib = int(fibonacci[i-2]) + int(fibonacci[i-1])
        fibonacci.append(fib)
    return fibonacci


listaFib = construirFib()
n = int(input())
for _ in range(n):
    x = int(input())
    print(f'Fib({x}) = {listaFib[x]}')
