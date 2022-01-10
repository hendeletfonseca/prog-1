def descobrirMaiorMenorUnidadesValor(lista):
    maior, menor = lista[0], lista[0]
    unidades, valor = 0, 0
    for i in range(len(lista)):
            if float(lista[i][3]) > float(maior[3]):
                maior = lista[i]
            if float(lista[i][3]) < float(menor[3]):
                menor = lista[i]
            unidades += int(lista[i][2])
            valor += float(lista[i][2]) * float(lista[i][3])
    return maior, menor, unidades, valor


def imprimirBonito(lista, baratoOuCaro):
    print(f'Produto Mais {baratoOuCaro}:', end=' (')
    for t in range(4):
        if t < 3 and type(lista[t]) == str:
            print(f"'{lista[t]}'", end=', ')
        if t < 3 and type(lista[t]) == int or t < 3 and type(lista[t]) == float:
            print(lista[t], end=', ')
        if t == 3:
            print(lista[t], end=')')
    return None


qtdProdutos = int(input())
if qtdProdutos == 0:
    print('Nenhum Produto foi Lido!!!')
else:
    produtos = []
    for _ in range(qtdProdutos):
        produtos.append(input().split('#'))
    maisCaro, maisBarato, qtdUnidades, valorEstoque = descobrirMaiorMenorUnidadesValor(produtos)
    maisCaro[2], maisCaro[3], maisBarato[2], maisBarato[3] = int(maisCaro[2]), float(maisCaro[3]), int(maisBarato[2]), float(maisBarato[3])
    imprimirBonito(maisBarato, 'Barato')
    print()
    imprimirBonito(maisCaro, 'Caro')
    print()
    print(f'Quantidade de Unidades no Mercado: {qtdUnidades}')
    print(f'Valor Total do Estoque: R$ {valorEstoque:.2f}')
