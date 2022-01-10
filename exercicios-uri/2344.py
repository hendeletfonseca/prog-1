# https://www.beecrowd.com.br/judge/pt/problems/view/2344

nota = int(input())
if nota == 0:
    print('E')
if 1<= nota <= 35:
    print('D')
if 36 <= nota <= 60:
    print('C')
if 61 <= nota <= 85:
    print('B')
if 86 <= nota <= 100:
    print('A')
