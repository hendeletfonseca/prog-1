# https://www.beecrowd.com.br/judge/pt/problems/view/2188

num_teste = 1
num_regioes = int(input())
while num_regioes != 0:
    x1, y1, x2, y2 = -100000, 100000, 100000, -100000
    for i in range(num_regioes):
        xMin, yMax, xMax, yMin = map(int, input().split())
        if xMin > x1:
            x1 = xMin
        if yMax < y1:
            y1 = yMax
        if xMax < x2:
            x2 = yMax
        if yMin > y2:
            y2 = yMin
    print(f'Teste {num_teste}')
    if x2 < x1 or y1 < y2:
        print('Nenhum')
    else:
        print(f'{x1} {y1} {x2} {y2}')
    num_teste += 1
    num_regioes = int(input())
