# https://www.beecrowd.com.br/judge/pt/problems/view/1507
# time limit exceed
# n = int(input())
# for _ in range(n):
#     sequencia = input()
#     qtdQ = int(input())
#     for _ in range(qtdQ):
#         querie = input()
#         aux = 0
#         palavra = ''
#         for i in sequencia:
#             if aux < len(querie):
#                 if i == querie[aux]:
#                     palavra += i
#                     aux += 1
#         if palavra == querie:
#             print('Yes')
#         else:
#             print('No')
def verificarSequencia(string, qre):
    count = 0
    seq = ''
    for i in range(len(string)):
        if string[i] == qre[count]:
            seq += string[i]
            count += 1
            if seq == qre:
                return True
    return False


for _ in range(int(input())):
    sequencia = input()
    for _ in range(int(input())):
        querie = input()
        if verificarSequencia(sequencia, querie):
            print('Yes')
        else:
            print('No')
