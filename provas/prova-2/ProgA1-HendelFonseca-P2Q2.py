# subprograms
def print_file(file, msg):
    print(msg)
    data = open(file, 'r', encoding='utf-8')
    for line in data:
        print(line.strip('\n'))
    data.close()
    print()
    return None


def add_new_product(file, product):
    from os import remove, rename
    data = open(file, 'r', encoding='utf-8')
    new_data = open(file + '$$$', 'w', encoding='utf-8')
    new_product_added = False
    for line in data:
        if alphabetic_ord(product, line) == product and not new_product_added:
            new_data.write(product + '\n')
            new_product_added = True  # altera o bool para que o novo produto não seja adicionado 2 vezes
        new_data.write(line)
    data.close()
    new_data.close()
    remove(file)
    rename(file + '$$$', file)
    return None


def alphabetic_ord(str1, str2):
    if len(str1) < len(str2):  # para nao apresentar index out of range
        for i in range(len(str1)):
            if ord(str1[i]) < ord(str2[i]):  # ord retorna um int que representa a str de len==1
                return str1
            elif ord(str1[i]) > ord(str2[i]):
                return str2
    else:
        for i in range(len(str1)):
            if ord(str1[i]) < ord(str2[i]):
                return str1
            elif ord(str1[i]) > ord(str2[i]):
                return str2
    return None


# main program
file_name = input('Digite o nome do arquivo: ')
new_product = input()
print_file(file_name, f'Conteúdo do {file_name} antes:')
add_new_product(file_name, new_product)
print_file(file_name, f'Conteúdo do {file_name} depois:')
