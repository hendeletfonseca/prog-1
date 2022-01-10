wrong, num = map(str, input().split())
while wrong != '0' and num != '0':
    temp_word = ''
    aux = False
    prints = 0
    for i in num:
        if wrong != i:
            temp_word += i
    size = len(temp_word)
    if temp_word == '':
        print(0)
    elif size == 1:
        print(int(temp_word))
    else:
        for ind in range(size):
            if temp_word[ind] != '0' or aux:
                aux = True
                print(temp_word[ind], end='')
        if not aux:
            print(0)
        else:
            print()
    wrong, num = map(str, input().split())
