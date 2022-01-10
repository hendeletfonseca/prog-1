# https://www.beecrowd.com.br/judge/pt/problems/view/1244

def ordenarPelaMaior(list):
    newList = []
    for e in list:
        ultimo = ''
        if len(newList) == 0:
            newList.append(e)
            ultimo = e
        for i in newList:
            if len(e) > len(i) and e not in newList:
                newList.insert(newList.index(i), e)
                ultimo = e
        if e not in newList:
            newList.append(e)
            ultimo = e
        elif e != ultimo:
            newList.append(e)
    return newList


tests = int(input())
listas = []
for _ in range(tests):
    words = input().split()
    listas.append(ordenarPelaMaior(words))
for i in range(len(listas)):
    print(*listas[i])
