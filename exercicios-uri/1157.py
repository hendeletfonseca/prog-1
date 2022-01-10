# https://www.beecrowd.com.br/judge/pt/problems/view/1157

def imprimirDivisor(num):
    for i in range(1, num+1):
        if num % i == 0:
            print(i)
    return


imprimirDivisor(int(input()))
