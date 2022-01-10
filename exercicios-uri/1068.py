# https://www.beecrowd.com.br/judge/pt/problems/view/1068

txt = input()
aberto = 0
fechado = 0
inicio_a = 0
inicio_f = 0
fim_a = txt.find('(', inicio_a)
fim_f = txt.find(')', inicio_f)

while fim_a != -1:
    aberto += 1
    inicio_a = fim_a + 1
    fim_a = txt.find('(', inicio_a)
while fim_f != -1:
    fechado += 1
    inicio_f = fim_f + 1
    fim_f = txt.find(')', inicio_f)
if fechado == aberto:
    print("correct")
else:
    print("incorrect")
