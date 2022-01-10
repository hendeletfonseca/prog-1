def mostraArquivoViaWhile(nm):
    print("Conteúdo do arquivo %s:" % nm)
    dados = open(nm, 'r', encoding='utf-8')
    linhaLida = dados.readline()
    while linhaLida != '':
        print(linhaLida)#.strip('\n'))
        linhaLida = dados.readline()
    dados.close()
    print()
    return None


def mostraArquivoViaFor(nm):
    print("Conteúdo do arquivo %s:" % nm)
    dados = open(nm, 'r', encoding='utf-8')
    for linhaLida in dados:
        print(linhaLida.strip('\n'))
    dados.close()
    print()
    return None


def criarArquivo(nm):
    dados = open(nm, 'w', encoding='utf-8')
    qtdLinhas = int(input())
    for i in range(qtdLinhas):
        novaLinha = input()
        dados.write(novaLinha+'\n')
    dados.close()
    return None


def anexarOuCriarArquivo(nm):
    dados = open(nm, 'a', encoding='utf-8')
    qtdLinhas = int(input())
    for i in range(qtdLinhas):
        novaLinha = input()
        dados.write(novaLinha + '\n')
    dados.close()
    return None


criarArquivo('simp2q2')
#código#preço#quantidade#dias restantes de validade