# https://www.beecrowd.com.br/judge/pt/problems/view/1180

def buscarMenor(lista, num):
    menorN = lista[0]
    for i in range(num):
        if lista[i] < menorN:
            menorN = lista[i]
    return menorN


n = int(input())
valores = list(map(int, input().split()))
menor = buscarMenor(valores, n)

print(f'Menor valor: {menor}')
print(f'Posicao: {valores.index(menor)}')



