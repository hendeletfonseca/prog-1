# https://www.beecrowd.com.br/judge/pt/problems/view/1042

entrada = input().split()
valores = [int(i) for i in entrada]
valores.sort()

print(*valores, sep='\n')
print()
print(*entrada, sep='\n')
