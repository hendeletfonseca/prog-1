# https://www.beecrowd.com.br/judge/pt/problems/view/1478

def construirMatriz(dimensao):
    matriz = []
    for _ in range(dimensao):
        linha = []
        for _ in range(dimensao):
            linha.append(0)
        matriz.append(linha)
    return matriz


def organizarMatriz(matriz):
    count = 1
    for i in range(len(matriz)):
        matriz[i][0] = i + 1
        matriz[0][i] = i + 1
        matriz[i][i] = 1
    while count != len(matriz):
        for t in range(len(matriz) - count):
            matriz[t][t+count] = count+1
            matriz[t+count][t] = count+1
        count += 1
    return matriz


def imprimirMatriz(matriz):
    for i in range(len(matriz)):
        for ind in range(len(matriz)):
            if matriz[i][ind] < 10 and ind != len(matriz):
                print(' ', end='')
                print(f'{matriz[i][ind]:^3}', end='')
            if 10 <= matriz[i][ind] < 100 and ind != len(matriz):
                print(' ', end='')
                print(f'{matriz[i][ind]:^3}', end='')
            if matriz[i][ind] == 100 and ind != len(matriz):
                print('', end='')
                print(f'{matriz[i][ind]:^3}', end=' ')
        print()
    return None


n = int(input())
while n != 0:
    imprimirMatriz(organizarMatriz(construirMatriz(n)))
    n = int(input())
