# https://www.beecrowd.com.br/judge/pt/problems/view/3171

def testarLigacoes(xs, ys, n):
    conectados = [xs[0], ys[0]]
    del xs[0]
    del ys[0]
    for _ in range(n - 1):
        for i in conectados:
            if i in xs:
                posx = xs.index(i)
            else:
                posx = -1
            if posx != -1:
                conectados.append(ys[posx])
                del xs[posx]
                del ys[posx]
            if i in ys:
                posy = ys.index(i)
            else:
                posy = -1
            if posy != -1:
                conectados.append(xs[posy])
                del xs[posy]
                del ys[posy]
    if len(conectados) == n:
        return True
    else:
        return False


n, l = map(int, input().split())
xs, ys = [], []
for _ in range(l):
    x, y = map(int, input().split())
    xs.append(x), ys.append(y)
situacao = testarLigacoes(xs, ys, n)
if situacao:
    print('COMPLETO')
else:
    print('INCOMPLETO')
