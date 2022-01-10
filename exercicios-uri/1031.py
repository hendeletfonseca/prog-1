# https://www.beecrowd.com.br/judge/pt/problems/view/1031

def criarRegiao(n):
    reg = []
    for j in range(n):
        reg.append(j+1)
    return reg


def arrumarEntradas():
    lista = list()
    n = int(input())
    while 13 <= n <= 100:
        lista.append(n)
        n = int(input())
    return lista


# main
resultados = list()
entradas = arrumarEntradas()
for i in entradas:
    jumporiginal = 1
    regioesoriginais = criarRegiao(i)
    m = 0
    while m == 0:
        index = 0
        removidos = list()
        regioes = regioesoriginais.copy()
        jump = jumporiginal
        while len(regioes) != 1:
            removidos.append(regioes[index])
            regioes.remove(regioes[index])
            if jumporiginal > len(regioes):
                jump = jumporiginal % len(regioes)
            if index+jump <= len(regioes):
                if jump == index == 0:
                    index = len(regioes)-1
                else:
                    index += jump - 1
            else:
                index = jump - (len(regioes) - index) - 1
        if regioes[0] == 13:
            resultados.append(jumporiginal)
            m = 1
        else:
            jumporiginal += 1
for b in resultados:
    print(b)
