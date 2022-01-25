def produz(nm):
    dicio_pals_0_cs = dict()
    dados = open(nm, 'r', encoding='utf-8')
    for linha in dados:
        palavras = linha.strip('\n').split()
        for pal in palavras:
            if dicio_pals_0_cs.get(pal) == None:
                dicio_pals_0_cs[pal] = 1
            else:
                dicio_pals_0_cs[pal] += 1
    dados.close()
    return dicio_pals_0_cs


def mostrar(dicio_pals_0_cs):
    print('Conteúdo do dicionário:')
    for chave, valor in dicio_pals_0_cs.items():
        print(' ', '%10s' % chave, 'ocorre', '%3d' % dicio_pals_0_cs[chave], 'vez(es)')
    return None


nome = input()
dicionario_de_palavras_com_contagem_de_ocorrencia = produz(nome)
mostrar(dicionario_de_palavras_com_contagem_de_ocorrencia)
