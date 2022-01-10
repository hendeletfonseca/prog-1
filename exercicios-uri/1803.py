# https://www.beecrowd.com.br/judge/pt/problems/view/1803

def construirMatriz():
    matriz = []
    for _ in range(4):
        linha = list(input())
        matriz.append(linha)
    return matriz


def calcularAscii(f, m, l):
    c = chr((int(f) * int(m) + int(l)) % 257)
    return c


matring = ''
matriz = construirMatriz()
for i in range(1, len(matriz[0]) - 1):
    f, l, m = '', '', ''
    for num in range(4):
        f += matriz[num][0]
        l += matriz[num][len(matriz[0])-1]
        m += matriz[num][i]
    matring += calcularAscii(f, m, l)
print(matring)
