# https://www.beecrowd.com.br/judge/pt/problems/view/1182

def construirMatriz():
    matriz = []
    for i in range(12):
        linha = []
        for e in range(12):
            linha.append(float(input()))
        matriz.append(linha)
    return matriz


c = int(input())
t = input()
matrizFinal = construirMatriz()
soma = 0
for a in range(12):
    soma += matrizFinal[a][c]
if t == 'S':
    print(f'{soma:.1f}')
else:
    print(f'{soma / 12:.1f}')
