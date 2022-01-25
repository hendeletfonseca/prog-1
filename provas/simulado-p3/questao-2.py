def produz(nm, minimo, maximo):
    produtos = dict()
    dados = open(nm, 'r', encoding='utf-8')
    for linha in dados:
        cod, des, qtd, preco = linha.strip('\n').split('#')
        if minimo <= float(preco) <= maximo:
            if produtos.get(cod) is None:
                produtos[cod] = [des, int(qtd), float(preco)]
            else:
                produtos[cod] = [des, int(qtd) + produtos[cod][1], float(preco) + produtos[cod][2]]
    dados.close()
    return produtos


def mostra(dic):
    codgs = []
    for val in dic:
        if codgs is None:
            codgs = [str(val)]
        else:
            codgs.append(str(val))
    sorted_codgs = sorted(codgs)
    for cod in sorted_codgs:
        print(f'Código: {cod} Descrição: {dic[str(cod)][0]} Produtos: {dic[str(cod)][1]} Preco: R${dic[str(cod)][2]}')
    return None


name = input()
min_len, max_len = map(float, input().split())
products = produz(name, min_len, max_len)
mostra(products)
