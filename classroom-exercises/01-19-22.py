def produz(lista_conj, lista_nm):
    for nm in lista_nm:
        novo_conjunto = set()
        dados = open(nm, 'r', encoding='utf-8')
        for linha in dados:
            palavras = linha.strip('\n').split()
            for palavra in palavras:
                novo_conjunto.add(palavra)
        dados.close()
        lista_conj.append(novo_conjunto)
    return None


def mostra_um_conjunto(conj_pals, msg):
    print(msg)
    for palavra in conj_pals:
        print('\t' + palavra)
    print()


def mostrar(lista_conj, lista_nms):
    for i in range(len(lista_nms)):
        mostra_um_conjunto(lista_conj[i], f'conjunto de palavras no arquivo {lista_nms[i]}')
    print()
    return None


def mostra_conjunto_uniao(lista_conj):
    uniao = set()
    for conj in lista_conj:
        uniao = uniao.union(conj)
    mostra_um_conjunto(uniao, f'conjunto uniao de palavras de todos os arquivos é:')
    return None


def mostra_conjunto_interseccao(lista_conj):
    interseccao = lista_conj[0]
    for conj in lista_conj[1:]:
        interseccao = interseccao.intersection(conj)
    mostra_um_conjunto(interseccao, f'conjunto interseccao de palavras de todos os arquivos é:')
    return None


nomes_de_arquivos = input().split()
lista_conjuntos = []
produz(lista_conjuntos, nomes_de_arquivos)
mostrar(lista_conjuntos, nomes_de_arquivos)
mostra_conjunto_uniao(lista_conjuntos)
mostra_conjunto_interseccao(lista_conjuntos)
