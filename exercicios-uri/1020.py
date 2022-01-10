# https://www.beecrowd.com.br/judge/pt/problems/view/1020
x = int(input())

ano = (x / 365)
mes = ((x % 365) / 30)
dia = ((x % 365) % 30)

print("%d ano(s)" % ano)
print("%d mes(es)" % mes)
print("%d dia(s)" % dia)
