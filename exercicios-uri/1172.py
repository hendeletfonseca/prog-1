# https://www.beecrowd.com.br/judge/pt/problems/view/1172

def construirLista():
    lista = []
    for _ in range(10):
        lista.append(int(input()))
    return lista


count = 0
x = construirLista()
for e in x:
    if e <= 0:
        x[count] = 1
    print(f'X[{count}] = {x[count]}')
    count += 1
