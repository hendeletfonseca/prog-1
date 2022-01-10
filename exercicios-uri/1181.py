# https://www.beecrowd.com.br/judge/pt/problems/view/1181

l = int(input())
t = input()
matriz = []
soma = 0

for i in range(12):
    linha = []
    for e in range(12):
         linha.append(float(input()))
    matriz.append(linha)

for num in matriz[l]:
    soma += num
if t == 'S':
    print(f'{soma:.1f}')
elif t == 'M':
    print(f'{soma/len(matriz[l])}')

