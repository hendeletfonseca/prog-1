# subprograms
def print_file(file, msg):
    print(msg)
    data = open(file, 'r', encoding='utf-8')
    for line in data:
        print(line.strip('\n'))
    data.close()
    print()
    return None


def reversing_word(file, reverse_word):
    from os import remove, rename
    inverted_word = ''
    for i in range(len(reverse_word) - 1, -1, -1):
        inverted_word += reverse_word[i]
    data = open(file, 'r', encoding='utf-8')
    new_data = open(file + '$$$', 'w', encoding='utf-8')
    for line in data:
        new_line = ''
        temp_word = ''
        for letter in line:
            if letter != ' ' and letter != '\n':
                temp_word += letter
            elif temp_word == reverse_word:
                new_line += ' ' + f'{inverted_word}'
                temp_word = ''
            else:
                new_line += ' ' + f'{temp_word}'
                temp_word = ''
        new_data.write(new_line + '\n')
    data.close()
    new_data.close()
    remove(file)
    rename(file + '$$$', file)
    return None


# main program
file_name = input('Digite o nome do arquivo: ')
word_to_reverse = input('Digite a palavra a inverter: ')
print_file(file_name, f'Arquivo {file_name} antes das inversões de {word_to_reverse}:')
reversing_word(file_name, word_to_reverse)
print_file(file_name, f'Arquivo {file_name} depois das inversões de {word_to_reverse}:')
