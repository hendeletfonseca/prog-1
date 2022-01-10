# https://www.beecrowd.com.br/judge/pt/problems/view/1171

def construirListas(num):
    lista = []
    numeros = []
    for i in range(num):
        x = int(input())
        lista.append(x)
        if x not in numeros:
            numeros.append(x)
    numeros.sort()
    return lista, numeros


todosNum, unicosNum = construirListas(int(input()))
for i in unicosNum:
    print(f'{i} aparece {todosNum.count(i)} vez(es)')
