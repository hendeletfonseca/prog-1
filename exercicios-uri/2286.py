# https://www.beecrowd.com.br/judge/pt/problems/view/2286

teste = 0
numeroPartidas = int(input())
while numeroPartidas != 0:
    teste += 1
    jogador1 = input()
    jogador2 = input()
    print(f'Teste {teste}')
    for _ in range(numeroPartidas):
        dedosJ1, dedosJ2 = map(int, input().split())
        if (int(dedosJ1) + int(dedosJ2)) % 2 == 0:
            print(jogador1)
        else:
            print(jogador2)
    print()
    numeroPartidas = int(input())
