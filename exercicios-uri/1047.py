# https://www.beecrowd.com.br/judge/pt/problems/view/1047

hi, mi, hf, mf = map(int, input().split())
h = 0
m = 0

if hf == hi and mf == mi:
    h = 24
    m = 0
elif hf == hi and mf > mi:
    h = hf - hi
    m = mf - mi
elif hf == hi and mf < mi:
    h = (hf + 23) - hi
    m = (mf + 60) - mi
elif hf > hi and mf > mi:
    h = hf - hi
    m = mf - mi
elif hf > hi and mf < mi:
    h = (hf - hi) - 1
    m = (mf + 60) - mi
elif hf > hi and mf == mi:
    h = (hf - hi)
    m = mf - mi
elif hf < hi and mf > mi:
    h = (hf + 24) - hi
    m = mf - mi
elif hf < hi and mf < mi:
    h = (hf + 23) - hi
    m = (mf + 60) - mi
elif hf < hi and mf == mi:
    h = (hf + 24) - hi
    m = (mf - mi)

print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" % (h, m))