def criar_dict(nm, minimo, maximo):
    all_words = dict()
    dados = open(nm, 'r', encoding='utf-8')
    line = 1
    for linha in dados:
        palavras = linha.strip('\n').split()
        for palavra in palavras:
            if minimo <= len(palavra) <= maximo:
                if all_words.get(palavra) is None:
                    all_words[palavra] = {line}
                else:
                    all_words[palavra].add(line)
        line += 1
    dados.close()
    return all_words


def mostrar(dic):
    for chave in sorted(dic):
        print(f'Chave: {chave}')
        print(f'Linha em que ela ocorre: {dic[chave]}')
        print()
    return None


nome = input()
min_len, max_len = map(int, input().split())
words = criar_dict(nome, min_len, max_len)
mostrar(words)
