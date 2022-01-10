# https://www.beecrowd.com.br/judge/pt/problems/view/1029

def fib(x):
    if x == 0:
       return 0
    if x == 1:
       return 1
    else:
        resp = fib(x-1) + fib(x-2)
    return int(resp)


entrada = int(input())
lista = []
num_calls = 0
while entrada > 0:
    n = (input())
    int(n)
    entrada -= 1
    lista = lista + list(n)

lista = list(map(int, lista))

for i in lista:
    print("fib(%d) = %d calls  = %d" % (i, num_calls, fib(i)))
