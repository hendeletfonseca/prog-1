def produz(nm, minimo, maximo):
    produtos = dict()
    dados = open(nm, 'r', encoding='utf-8')
    for linha in dados:
        cod, des, qtd, preco = linha.strip('\n').split('#')
        if minimo <= float(preco) <= maximo:
            produtos[cod] = [des, int(qtd), float(preco)]
    dados.close()
    return produtos


def mostra(dic):
    print('Produtos dentro do intervalo de preços desejado:')
    for cod in sorted(dic):
        print(f'Código: {cod} Descrição: {dic[cod][0]} Produtos: {dic[cod][1]} Preco: R${dic[cod][2]}')
    return None


name = input()
min_len, max_len = map(float, input().split())
products = produz(name, min_len, max_len)
mostra(products)
