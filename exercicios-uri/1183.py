# https://www.beecrowd.com.br/judge/pt/problems/view/1183

def construirMatriz():
    matriz = []
    for i in range(12):
        linha = []
        for e in range(12):
            linha.append(float(input()))
        matriz.append(linha)
    return matriz


o = input()
matrizFinal = construirMatriz()
soma = 0
for i in range(11):
    for ind in range(i+1, 12):
        soma += (matrizFinal[i][ind])
media = soma/66
if o == 'S':
    print(f'{soma:.1f}')
if o == 'M':
    print(f'{media:.1f}')
