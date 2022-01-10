# https://www.beecrowd.com.br/judge/pt/problems/view/1117

def valindando_notas(x):
    if 0 <= x <= 10:
        return True
    else:
        print("nota invalida")
        return False


qtdNotas = 0
notas = 0
while qtdNotas != 2:
    nota = float(input())
    vdd = valindando_notas(nota)
    if vdd:
        qtdNotas += 1
        notas += nota
print('media = %.2f' % (notas/2))
