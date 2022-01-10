# https://www.beecrowd.com.br/judge/pt/problems/view/2231

N, M = map(int, input().split())
k = 0
while N != 0 and M != 0:
    k += 1
    L = []
    menor = 201
    maior = -201
    # lê as temperaturas
    for i in range(N):
        L.append(int(input()))

    # calcula somas acumuladas
    acum = []
    soma = 0
    for i in range(N):
        soma += L[i]
        acum.append(soma)

    # calcula as médias
    for j in range(M-1, N):
        s = 0
        # soma as temperaturas em cada intervalo
        if j-M < 0:
            s = acum[j]
        else:
            s = acum[j]-acum[j-M]
            media = int(s/M)
            if media < menor:
                menor = media
            if media > maior:
                maior = media

    print("Teste", k)
    print(menor, maior)
    print()
    N, M = map(int, input().split())
