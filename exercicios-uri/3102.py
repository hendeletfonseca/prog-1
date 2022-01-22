# https://www.beecrowd.com.br/judge/pt/problems/view/3102
test_cases = int(input())
for i in range(test_cases):
    xa, ya, xb, yb, xc, yc = map(int, input().split())
    area = abs((xa*yb + ya*xc + xb*yc) - (ya*xb + xa*yc + yb*xc))*0.5
    print(f'{area:.3f}')
