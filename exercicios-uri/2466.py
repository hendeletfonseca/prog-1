# https://www.beecrowd.com.br/judge/pt/problems/view/2466
# preta (1) branca (-1) / iguais-preta diferentes-branca
num_balls = int(input())
last_line = list(map(int, input().split()))
while len(last_line) > 1:
    temp_line = []
    for i in range(len(last_line) - 1):
        if last_line[i] == last_line[i+1]:
            temp_line.append(int(1))
        elif last_line[i] != last_line[i+1]:
            temp_line.append(int(-1))
    last_line = temp_line
if last_line[0] == 1:
    print('preta')
if last_line[0] == -1:
    print('branca')
