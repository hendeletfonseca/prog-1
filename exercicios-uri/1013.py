# https://www.beecrowd.com.br/judge/pt/problems/view/1013

a, b, c = map(int, input().split())

teste = (a + b + abs(a - b))/2
maior = (teste + c + abs(teste - c))/2

print("%d eh o maior" % maior)
