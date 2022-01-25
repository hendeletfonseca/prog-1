def criar_dict(nm, min, max):
    all_words = dict()
    dados = open(nm, 'r', encoding='utf-8')
    line = 1
    for linha in dados:
        palavras = linha.strip('\n').split()
        for palavra in palavras:
            if min <= len(palavra) <= max:
                if all_words.get(palavra) == None:
                        all_words[palavra] = {line}
                else:
                    all_words[palavra].add(line)
        line += 1
    dados.close()
    return all_words


def mostrar(dic):
    for chave in dic:
        print(f'Chave: {chave}')
        print(f'Linha em que ela ocorre: {dic[chave]}')
        print()
    return None


nome = input()
min_len, max_len = map(int, input().split())
words = criar_dict(nome, min_len, max_len)
mostrar(words)
