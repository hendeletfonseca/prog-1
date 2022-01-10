# https://www.beecrowd.com.br/judge/pt/problems/view/1173

def construirVetor(num):
    lista = []
    for i in range(10):
        if i == 0:
            lista.append(num)
        else:
            lista.append(lista[i-1] * 2)
    return lista


count = 0
n = construirVetor(int(input()))
for i in range(len(n)):
    print(f'N[{i}] = {n[i]}')
