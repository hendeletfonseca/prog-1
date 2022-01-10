# https://www.beecrowd.com.br/judge/pt/problems/view/3182

participantes, orcamento, hoteis, semanas = map(int, input().split())
preco = []
camas = []
maisBarato = orcamento+1
for _ in range(hoteis):
    preco.append(int(input()))
    cama = input().split()
    camas.append(cama)
for i in range(len(camas)):
    for cama in camas[i]:
        if int(cama) >= participantes:
            temp_preco = preco[i] * participantes
            if temp_preco < maisBarato:
                maisBarato = temp_preco
if maisBarato <= orcamento:
    print(f'{maisBarato}')
else:
    print(f'stay home')