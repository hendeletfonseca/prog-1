# https://www.beecrowd.com.br/judge/pt/problems/view/1259

pares = []
impares = []
for _ in range(int(input())):
    num = int(input())
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
pares.sort()
impares.sort(reverse=True)
for i in range(len(pares)):
    print(pares[i])
for ind in range(len(impares)):
    print(impares[ind])
