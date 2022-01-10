def construirMatriz0(qtdL, qtdC):
    matriz = []
    for l in range(qtdL):
        linha = []
        for c in range(qtdC):
            linha.append(0)
        matriz.append(linha)
    return matriz


def novosValoresMatriz(matriz, valMin, valMax):
    from random import randint
    for l in range(len(matriz)):
        for c in range(len(matriz[l])):
            matriz[l][c] = randint(valMin, valMax)
    return matriz


def calculaMediaValores(matriz):
    soma = 0
    for l in range(len(matriz)):
        for c in range(len(matriz[l])):
            soma += int(matriz[l][c])
    mediaValores = soma / (len(matriz) * len(matriz[0]))
    return mediaValores


def imprimiBonito(matriz):
    for l in range(len(matriz)):
        print('   ', end='')
        for c in range(len(matriz)):
            print(matriz[l][c], end='   ')
        print()
    print()
    return None


tentativas = 0
matrizFinal = []
qtdLinhas, qtdColunas = map(int, input().split())
valMinimo, valMaximo = map(int, input().split())
limiteMinimo = float(input())
media = limiteMinimo - 1
while media < limiteMinimo and tentativas < 1000000:
    tentativas += 1
    matrizZero = construirMatriz0(qtdLinhas, qtdColunas)
    matrizFinal = novosValoresMatriz(matrizZero, valMinimo, valMaximo)
    media = calculaMediaValores(matrizFinal)
if media >= limiteMinimo:
    print(f'Conteúdo da Matriz:')
    imprimiBonito(matrizFinal)
    print(f'Limite da Média para Parar a Repetição: {limiteMinimo:.2f}')
    print(f'Média dos Valores da Matriz: {media:.2f}')
    print(f'Quantidade de tentativas para a média superar o limite mínimo: {tentativas}')
if tentativas == 1000000 and media < limiteMinimo:
    print('Após 1000000 de Tentativas, Nenhuma Média Superou o Limite Mínimo!!!')
