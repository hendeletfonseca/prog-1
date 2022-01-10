# https://www.beecrowd.com.br/judge/pt/problems/view/1043

entrada = input().split()
lado = [float(i) for i in entrada]
lado.sort(reverse=True)
lado1 = [float(i) for i in entrada]
perimetro = lado[0] + lado[1] + lado[2]
area = (lado1[0] + lado1[1]) * lado1[2] / 2

if lado[1] - lado[2] < lado[0] < lado[1] + lado[2]:
    print("Perimetro = %1.1f" % perimetro)
else:
    print("Area = %1.1f" % area)