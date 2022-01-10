# https://www.beecrowd.com.br/judge/pt/problems/view/2464

alfabeto = 'abcdefghijklmnopqrstuvwxyz'
permutacao = input()
for letra in input():
    print(alfabeto[permutacao.index(letra)], end='')
print()