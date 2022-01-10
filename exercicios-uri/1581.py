# https://www.beecrowd.com.br/judge/pt/problems/view/1581

n = int(input())
s = ""
ingles = 0
outro = 0

while n != 0:
    n -= 1
    k = int(input())
    while k != 0:
        k -= 1
        string = input()
        if s == "":
            s = string
        elif s == string and s != "ingles":
            outro += 1
        elif s == "ingles" or s != string:
            ingles += 1
    if ingles > 0:
        print("ingles")
        s = ""
        ingles = 0
    else:
        print(s)
        s = ""
        ingles = 0