""" def verificaPA(lista):
    razao = None
    for i in range(len(lista)):
        if razao == None:
            razao = lista[i+1] - lista[i]
        else:
            if (lista[i+1] - lista[i]) != razao:
                return False
    return True

tamanho = int(input())
sequencia = list(map(int, input().split()))
quebras = 1
if verificaPA(sequencia):
    print(1)
else:
     """