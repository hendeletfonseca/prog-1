# https://www.beecrowd.com.br/judge/pt/problems/view/1064

a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
lista = [a, b, c, d, e, f]
positivos = 0
media = 0

for i in lista:
    if i >= 0:
        positivos += 1
        media += i
    else:
        positivos = positivos

media = media / positivos
print("%d valores positivos" % positivos)
print("%.1f" % media)
