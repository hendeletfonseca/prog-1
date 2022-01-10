# https://www.beecrowd.com.br/judge/pt/problems/view/1174

def construirVetor():
    lista = []
    for i in range(10):
        lista.append(float(input()))
    return lista


def imprimir(lista):
    for i in range(len(lista)):
        if lista[i] <= 10:
            print(f'A[{i}] = {lista[i]:.1f}')
    return None


a = construirVetor()
imprimir(a)
