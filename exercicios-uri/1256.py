# https://www.beecrowd.com.br/judge/pt/problems/view/1256
test_cases = int(input())
for case in range(test_cases):
    lists = [[]]
    qtd_address, qtd_keys = map(int, input().split())
    keys = list(map(int, input().split()))
    for _ in range(qtd_address):
        lists[0].append([])
    for key in keys:
        pos = key % qtd_address
        lists[0][pos].append(key)
    for i in range(qtd_address):
        if len(lists[0][i]) == 0:
            numbers = '\\'
        else:
            numbers = lists[0][i]
        print(f'{i} -> ', end='')
        print(*numbers, sep=' -> ', end='')
        if numbers != '\\':
            print(' -> \\')
        else:
            print()
    if case != test_cases - 1:
        print()
