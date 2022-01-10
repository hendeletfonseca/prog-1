# https://www.beecrowd.com.br/judge/pt/problems/view/1609
# def quantosCarneiros(seq):
#     unicos = ''
#     for num in seq:
#         if num not in unicos:
#             unicos += num
#     print(len(unicos))
#     return None
#
#
# for _ in range(int(input())):
#     quantidade = int(input())
#     sequencia = input().split()
#     quantosCarneiros(sequencia)
for _ in range(int(input())):
    quantidade = int(input())
    sequencia = input().split()
    print(len(set(sequencia)))