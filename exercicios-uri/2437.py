# https://www.beecrowd.com.br/judge/pt/problems/view/2437

xm, ym, xr, yr = map(int, input().split())
print(f'{abs(xm-xr)+abs(ym-yr)}')