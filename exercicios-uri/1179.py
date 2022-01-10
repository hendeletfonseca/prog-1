# https://www.beecrowd.com.br/judge/pt/problems/view/1179

par = []
impar = []

for i in range(15):
    a = int(input())
    if a % 2 == 0:
        if len(par) < 4:
            par.append(a)
        elif len(par) == 4:
            par.append(a)
            for e in range(5):
                print('par[%d] = %d' % (e, par[e]))
            par = []

    if a % 2 != 0:
        if len(impar) < 4:
            impar.append(a)
        elif len(impar) == 4:
            impar.append(a)
            for t in range(5):
                print('impar[%d] = %d' % (t, impar[t]))
            impar = []

for index in range(len(impar)):
    print('impar[%d] = %d' % (index, impar[index]))
for n in range(len(par)):
    print('par[%d] = %d' % (n, par[n]))
